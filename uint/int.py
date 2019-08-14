from __future__ import annotations
import operator

from uint import Uint


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


