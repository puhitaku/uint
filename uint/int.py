from __future__ import annotations
import operator

from uint import Uint
from uint.util import twocomp, generate_bitmask


class Int(Uint):
    def __init__(self, value: int, bits: int):
        super().__init__(value, bits)

        # we replace self.raw as Uint's __init__ doesn't accept negative value
        self.raw = value

        self.signed = True
        self.me = 'int'

    @property
    def raw(self):
        return self._raw

    @raw.setter
    def raw(self, value):
        if self.is_twocomp(value):
            self._raw = -twocomp(value & self.mask, width=self.bits)
        else:
            self._raw = value & self.mask

    @property
    def native(self):
        if self._raw < 0:
            return twocomp(self._raw, self.bits)
        else:
            return self._raw

    def __str__(self) -> str:
        return f'<int{self.bits}, value={self.raw}>'

    def __neg__(self):
        return self._calc_alone(operator.inv) + 1

    def __rshift__(self, shift):
        def rshift(v):
            if self.is_twocomp(v):
                return generate_bitmask(self.bits) & (v >> shift)
            else:
                return v >> shift
        return self._calc_alone(rshift)

    def is_twocomp(self, v):
        return bool(v & (1 << (self.bits - 1)))
