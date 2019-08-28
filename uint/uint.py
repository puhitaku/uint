from __future__ import annotations

import copy
import math
import operator
from typing import Callable, Union

from uint.util import generate_bitmask, twocomp


class Uint:
    _raw: int = 0

    def __init__(self, value: int, bits: int):
        """Initialize Uint.

        Args:
            value (int): the first assigned value.
            bits (int): bit length.
        """

        self.bits = bits
        self.mask = generate_bitmask(bits)
        self.assign(value)

    # ---------- Public methods / properties

    """
    `raw` is for "raw signed int".
    `native` is for "CPU-native two's complementary int".

    For Uint, the value is unsigned so `raw` and `native` are identical:

    Uint(0x01, 8).raw -> 1
    Uint(0x01, 8).native -> 1

    Uint(0x90, 8).raw -> 144
    Uint(0x90, 8).native -> 144

    For Int, they become different according to its sign:

    Int(0x01, 8).raw -> 1
    Int(0x01, 8).native -> 1

    Int(0x90, 8).raw -> -112
    Int(0x90, 8).native -> 144
    """

    @property
    def raw(self):
        return self._raw

    @property
    def native(self):
        return self._raw

    def assign(self, value: int):
        if value < 0:
            value = twocomp(value, self.bits)
        self._raw = value & self.mask

    @property
    def literal(self):
        """Shorthand to format the value with Python literal syntax."""

        binw = self.bits + 2
        octw = math.ceil(self.bits / 3) + 2
        hexw = math.ceil(self.bits / 4) + 2

        class Literal:
            bin = ("{raw:#0%db}" % binw).format(raw=self.native)
            oct = ("{raw:#0%do}" % octw).format(raw=self.native)
            dec = str(self.raw)  # no modification is needed
            hex = ("{raw:#0%dx}" % hexw).format(raw=self.native)
        return Literal

    @property
    def wire(self):
        """Shorthand to format the value with Verilog wire syntax. """

        binw = self.bits
        octw = math.ceil(self.bits / 3)
        hexw = math.ceil(self.bits / 4)
        bits = str(self.bits)

        class Wire:
            bin = (bits + "'b{raw:0%db}" % binw).format(raw=self.native)
            oct = (bits + "'o{raw:0%do}" % octw).format(raw=self.native)
            dec = (bits + "'d{raw}").format(raw=self.native)
            hex = (bits + "'h{raw:0%dx}" % hexw).format(raw=self.native)
        return Wire

    # ---------- Private methods

    def _calc(self, other: Union[Uint, int], op: Callable[[int, int], int]) -> Union[Uint, bool]:
        """Calculates `self.val` and the `other` with binary func `op` then returns the copied result."""

        if issubclass(type(other), type(self)) or issubclass(type(self), type(other)):
            value = other.raw  # read raw via other (Uint, Int) property to affect sign
        elif isinstance(other, int):
            value = other
        else:
            raise TypeError(f"unsupported operand type(s): 'Uint' and '{type(other)}'")

        value = op(self.raw, value)

        if isinstance(value, bool):
            return value

        newself = copy.deepcopy(self)
        newself.assign(value)
        return newself

    def _calc_alone(self, op: Callable[[int], int]) -> Uint:
        """Calculates `self.val` with unary func `op` then returns the copied result."""

        newself = copy.deepcopy(self)
        newself.assign(op(self.raw))
        return newself

    # ---------- Misc. magic methods

    def __str__(self) -> str:
        return f'<uint{self.bits}, value={self.raw}>'

    def __repr__(self):
        return self.__str__()

    def __format__(self, fmt):
        fmt = '{v:%s}' % fmt
        return fmt.format(v=self.raw)

    # ---------- Operator implementations

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

    def __bool__(self):
        return bool(self.raw)

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

    def __int__(self):
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
        return self._calc_alone(lambda v: self.mask - self.raw + 1)

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
