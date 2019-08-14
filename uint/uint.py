from __future__ import annotations

import copy
import math
import operator
from typing import Callable, Union


class Uint:
    me: str = 'uint'
    signed: bool = False

    def __init__(self, value: int, bits: int):
        self.bits = bits
        self.mask = 2 ** bits - 1
        self.raw = value  # may be twocomp'd in `raw` property setter

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
        if self.signed and value < 0:
            value = self.mask + value + 1
        self._raw = value & self.mask

    def _calc(self, other: Union[Uint, int], op: Callable[[int, int], int]) -> Union[Uint, bool]:
        if issubclass(type(other), type(self)):
            value = other.raw  # read raw via other (Uint, Int) property to affect sign
        elif isinstance(other, int):
            value = other
        else:
            raise TypeError(f"unsupported operand type(s): 'Uint' and '{type(other)}'")

        value = op(self.raw, value)

        if isinstance(value, bool):
            return value

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
