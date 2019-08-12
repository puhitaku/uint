from __future__ import annotations

import copy
import math
import operator
from dataclasses import dataclass
from typing import Callable, List, Union


class Uint:
    me: str = 'uint'
    signed: bool = False

    def __init__(self, value: int, bits: int):
        self.bits = bits
        self.mask = 2 ** bits - 1
        self._raw = value

    @property
    def literal(self):
        binw = self.bits + 2
        octw = math.ceil(self.bits / 3) + 2
        hexw = math.ceil(self.bits / 4) + 2

        class Literal:
            bin = ("{raw:#0%db}" % binw).format(raw=self.raw)
            oct = ("{raw:#0%do}" % octw).format(raw=self.raw)
            dec = str(self.raw)
            hex = ("{raw:#0%dx}" % hexw).format(raw=self.raw)
        return Literal

    @property
    def wire(self):
        binw = self.bits
        octw = math.ceil(self.bits / 3)
        hexw = math.ceil(self.bits / 4)
        bits = str(self.bits)

        class Wire:
            bin = (bits + "'b{raw:0%db}" % binw).format(raw=self.raw)
            oct = (bits + "'o{raw:0%do}" % octw).format(raw=self.raw)
            dec = (bits + "'d{raw}").format(raw=self.raw)
            hex = (bits + "'h{raw:0%dx}" % hexw).format(raw=self.raw)
        return Wire

    def __str__(self) -> str:
        return f'<uint{self.bits}, value={self.raw}>'

    def __repr__(self):
        return self.__str__()

    @property
    def raw(self) -> int:
        return self._raw

    @raw.setter
    def raw(self, value):
        self._raw = value & self.mask

    def _calc(self, other: Union[Uint, int], op: Callable[[int, int], int]) -> Uint:
        if issubclass(type(other), type(self)):
            value = other.raw
        elif isinstance(other, int):
            value = other
        else:
            raise TypeError(f"unsupported operand type(s): 'Uint' and '{type(other)}'")

        value = op(self.raw, value)
        if not self.signed and value < 0:
            value = self.mask - (-value) + 1

        newself = copy.deepcopy(self)
        newself.raw = value
        return newself

    def _calc_alone(self, op: Callable[[int], int]) -> Uint:
        newself = copy.deepcopy(self)
        newself.raw = op(self.raw)
        return newself

    def __format__(self, fmt):
        fmt = '{v:%s}' % fmt
        return fmt.format(v=self.raw)

    def __lt__(self, other):
        return self._calc(other, operator.lt)

    def __le__(self, other):
        return self._calc(other, operator.le)

    def __eq__(self, other):
        return self._calc(other, operator.eq)

    def __ne__(self, other):
        return self._calc(other, operator.ne)

    def __ge__(self, other):
        return self._calc(other, operator.ge)

    def __gt__(self, other):
        return self._calc(other, operator.gt)

    def __truth__(self):
        return operator.truth(self.raw)

    def __abs__(self):
        return self._calc_alone(operator.abs)

    def __add__(self, other):
        return self._calc(other, operator.add)

    def __and__(self, other):
        return self._calc(other, operator.and_)

    def __floordiv__(self, other):
        return self._calc(other, operator.floordiv)

    def __index__(self):
        return self.raw

    def __invert__(self):
        return self._calc_alone(operator.inv)

    def __lshift__(self, other):
        return self._calc(other, operator.lshift)

    def __mod__(self, other):
        return self._calc(other, operator.mod)

    def __mul__(self, other):
        return self._calc(other, operator.mul)

    def __matmul__(self, other):
        raise TypeError('matmul is unsupported')

    def __neg__(self):
        raise TypeError('neg is unsupported as it is unsigned')

    def __or__(self, other):
        return self._calc(other, operator.or_)

    def __pos__(self):
        return self

    def __pow__(self, other):
        return self._calc(other, operator.pow)

    def __rshift__(self, other):
        return self._calc(other, operator.rshift)

    def __sub__(self, other):
        return self._calc(other, operator.sub)

    def __truediv__(self, other):
        raise TypeError('truediv is impossible')

    def __xor__(self, other):
        return self._calc(other, operator.xor)


class Int(Uint):
    def __init__(self, value: int, bits: int):
        super().__init__(value, bits)
        self.signed = True
        self.me = 'int'

    def is_negative(self):
        return super().raw & (1 << (self.bits - 1))

    @property
    def raw(self):
        if self.is_negative():
            return ~super().raw + 1
        else:
            return super().raw

    @raw.setter
    def raw(self, value):
        self._raw = value & self.mask

    def __repr__(self):
        return f'<int{self.bits}, value={self.raw}>'

    def __neg__(self):
        return self._calc_alone(operator.inv) + 1


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

