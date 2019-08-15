from __future__ import annotations
import operator

from uint import Uint


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
            self._raw = -self.twocomp(value & self.mask)
        else:
            self._raw = value & self.mask

    @property
    def native(self):
        if self._raw < 0:
            return self.twocomp(self._raw)
        else:
            return self._raw

    def __str__(self) -> str:
        return f'<int{self.bits}, value={self.raw}>'

    def __neg__(self):
        return self._calc_alone(operator.inv) + 1

    def twocomp(self, v):
        if v < 0:
            v = -v
        return self.mask - v + 1

    def is_twocomp(self, v):
        return bool(v & (1 << (self.bits - 1)))
