from dataclasses import dataclass
from typing import List

from uint import Uint


@dataclass
class Field:
    name: str
    index: slice
    value: Uint


class Register:
    @dataclass
    class _RegisterFieldAccessor:
        _f: Field

        def __setitem__(self, index, value):
            self._f.value = value

    def __init__(self, register_name):
        self.name = register_name
        self.fields: List[Field] = []

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
                f.value.raw = value
                return
            else:
                raise ValueError(f'Field "{index}" is not defined.')

        # pattern 2: defining new field
        if isinstance(index, slice):
            pass
        elif isinstance(index, int):
            index = slice(index, index)
        else:
            raise ValueError(f'Invalid index type.')

        if isinstance(value, int) or issubclass(type(value), Uint):
            raise TypeError('Cannot specify a value directly on a range.')
        elif not isinstance(value, str):
            raise TypeError(f'Invalid type {type(value)}. Pass str to assign new field.')

        leftmost, rightmost = max(index.start, index.stop), min(index.start, index.stop)
        field = Field(value, slice(leftmost, rightmost), Uint(0, leftmost - rightmost + 1))
        self.fields.append(field)

    def __len__(self):
        return max(max(f.index.start, f.index.stop) for f in self.fields)

    def __repr__(self):
        return f'<register "{self.name}">'

    def _get_field(self, field_name):
        for f in self.fields:
            if f.name == field_name:
                return f
        return None

    def encode(self):
        acc = 0
        for f in self.fields:
            shifted = f.value.raw << f.index.stop
            acc |= shifted
        return acc

    def decode(self, raw):
        # idx: 8 7 6 5 4 3 2 1 0
        # sli: x x x x 4 x x 1 x
        for f in self.fields:
            width = f.index.start - f.index.stop + 1
            cut = raw >> f.index.stop
            cut &= int('1' * width, 2)
            f.value = Uint(cut, width)

