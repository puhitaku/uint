from __future__ import annotations
import operator

from uint import Uint
from uint.util import twocomp, is_twocomp, generate_bitmask


class Int(Uint):
    _raw = 0

    def __init__(self, value: int, bits: int):
        super().__init__(value, bits)

        # we replace self.raw as Uint's __init__ doesn't accept negative value
        self.assign(value)

        self.signed = True
        self.me = 'int'

    # ---------- Public methods / properties

    """For the difference between `raw` and `native`, please refer to uint.py."""

    @property
    def raw(self):
        return self._raw

    @property
    def native(self):
        if self._raw < 0:
            return twocomp(self._raw, self.bits)
        else:
            return self._raw

    def assign(self, value):
        if is_twocomp(value, self.bits):
            self._raw = -twocomp(value & self.mask, width=self.bits)
        else:
            self._raw = value & self.mask

    # ---------- Misc. magic methods

    def __str__(self) -> str:
        return f'<int{self.bits}, value={self.raw}>'

    # ---------- Operator implementations

    def __neg__(self):
        return self._calc_alone(operator.inv) + 1

    def __rshift__(self, shift):
        def rshift(v):
            if is_twocomp(v, self.bits):
                return generate_bitmask(self.bits) & (v >> shift)
            else:
                return v >> shift
        return self._calc_alone(rshift)

