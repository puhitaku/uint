from dataclasses import dataclass
from typing import List

from uint import Uint
from uint.util import generate_bitmask


@dataclass
class Field:
    name: str
    index: slice
    value: Uint


class Register:
    name: str = None
    _fields: List[Field] = None

    class OverlappedRange(Exception):
        pass

    def __init__(self, register_name):
        self.name = register_name
        self._fields = []

    def __getitem__(self, field_name):
        f = self._get_field(field_name)
        if f:
            return f
        else:
            raise ValueError(f'Field "{field_name}" is not defined.')

    def __setitem__(self, index, value):
        # pattern 1: defining value of known register (index is a field name)
        if isinstance(index, str):
            f = self._get_field(index)
            if f:
                f.value.assign(value)
                return
            else:
                raise ValueError(f'Field "{index}" is not defined.')

        # pattern 2: defining new field
        if isinstance(index, slice):
            f = self._check_overlap(index)
            if f is not None:
                raise self.OverlappedRange(
                    f'[{index.start}:{index.stop}] overlaps to {f.name}[{f.index.start}:{f.index.stop}].')
        elif isinstance(index, int):
            index = slice(index, index)
            f = self._check_overlap(index)
            if f is not None:
                raise self.OverlappedRange(
                    f'[{index.start}:{index.stop}] overlaps to {f.name}[{f.index.start}:{f.index.stop}].')
        else:
            raise ValueError(f'Invalid index type.')

        if isinstance(value, int) or issubclass(type(value), Uint):
            raise TypeError('Cannot specify a value directly on a range.')
        elif not isinstance(value, str):
            raise TypeError(f'Invalid type {type(value)}. Pass str to assign new field.')

        leftmost, rightmost = max(index.start, index.stop), min(index.start, index.stop)
        field = Field(value, slice(leftmost, rightmost), Uint(0, leftmost - rightmost + 1))
        self._fields.append(field)

    def __len__(self):
        return max(f.index.start for f in self._fields) + 1

    def __repr__(self):
        return f'<register "{self.name}">'

    def _check_overlap(self, sl):
        for f in self._fields:
            if f.index.start >= sl.start >= f.index.stop:
                return f
            elif f.index.start >= sl.stop >= f.index.stop:
                return f
        return None

    def _get_field(self, field_name):
        for f in self._fields:
            if f.name == field_name:
                return f
        return None

    @property
    def fields(self):
        return self._fields

    def encode(self):
        acc = 0
        for f in self._fields:
            shifted = f.value.raw << f.index.stop
            acc |= shifted
        return acc

    def decode(self, raw):
        # idx: 8 7 6 5 4 3 2 1 0
        # sli: x x x x 4 x x 1 x
        for f in self._fields:
            width = f.index.start - f.index.stop + 1
            cut = raw >> f.index.stop
            cut &= generate_bitmask(width)
            f.value = Uint(cut, width)
