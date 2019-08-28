import pytest
from uint import Uint


def test_positive_overflow():
    u = Uint(0b11111111, 8)
    u += 1
    assert u.raw == 0b00000000


def test_negative_overflow():
    u = Uint(0b00000000, 8)
    u -= 1
    assert u.raw == 0b11111111


def test_logical_shift():
    u = Uint(0b10100101, 8)
    u <<= 1
    assert u.raw == 0b01001010
    u >>= 2
    assert u.raw == 0b00010010


def test_fmt_literal():
    u = Uint(0xDEADBEEF, 32)
    assert u.literal.bin == f'{0xDEADBEEF:#34b}'
    assert u.literal.oct == f'{0xDEADBEEF:#13o}'
    assert u.literal.dec == f'{0xDEADBEEF}'
    assert u.literal.hex == f'{0xDEADBEEF:#10x}'


def test_fmt_wire():
    u = Uint(0xDEADBEEF, 32)
    assert u.wire.bin == f"32'b{0xDEADBEEF:032b}"
    assert u.wire.oct == f"32'o{0xDEADBEEF:011o}"
    assert u.wire.dec == f"32'd{0xDEADBEEF}"
    assert u.wire.hex == f"32'h{0xDEADBEEF:08x}"


def test_public_api():
    """
    Exposed functions are:
     - raw -> int, returns unsigned number
     - native -> int, same as `raw`
     - literal.bin -> str, Python literal representation (binary)
     - literal.oct -> str, Python literal representation (octal)
     - literal.dec -> str, Python literal representation (decimal)
     - literal.hex -> str, Python literal representation (hexadecimal)
     - wire.bin -> str, Verilog wire representation (binary)
     - wire.oct -> str, Verilog wire representation (octal)
     - wire.dec -> str, Verilog wire representation (decimal)
     - wire.hex -> str, Verilog wire representation (hexadecimal)
    """
    u = Uint(0x5a, 8)
    assert u.raw == 0x5a
    assert u.native == 0x5a
    assert u.literal.bin == "0b01011010"
    assert u.literal.oct == "0o132"
    assert u.literal.dec == "90"
    assert u.literal.hex == "0x5a"
    assert u.wire.bin == "8'b01011010"
    assert u.wire.oct == "8'o132"
    assert u.wire.dec == "8'd90"
    assert u.wire.hex == "8'h5a"


def test_assign():
    u = Uint(0, 8)
    u.assign(0xff)
    assert u.raw == 0xff
    u.assign(-1)
    assert u.raw == 0xff


def test_minus():
    u = Uint(0x01, 8)
    u = -u
    assert u.raw == 0xff


def test_lt():
    x, y = Uint(0x01, 8), Uint(0x02, 8)
    m = Uint(-1, 8)
    assert x < y
    assert not y < x
    assert not x < x
    assert x < m


def test_le():
    x, y = Uint(0x01, 8), Uint(0x02, 8)
    m = Uint(-1, 8)
    assert x <= y
    assert not y <= x
    assert x <= x
    assert x <= m


def test_eq():
    x, y = Uint(1, 8), Uint(2, 8)
    m, n = Uint(-1, 8), Uint(255, 8)
    assert x == x
    assert not x == y
    assert m == n


def test_ne():
    x, y = Uint(1, 8), Uint(2, 8)
    m, n = Uint(-1, 8), Uint(255, 8)
    assert not x != x
    assert x != y
    assert not m != n


def test_ge():
    x, y = Uint(0x01, 8), Uint(0x02, 8)
    m = Uint(-1, 8)
    assert not x >= y
    assert y >= x
    assert x >= x
    assert not x >= m


def test_gt():
    x, y = Uint(0x01, 8), Uint(0x02, 8)
    m = Uint(-1, 8)
    assert not x > y
    assert y > x
    assert not x > x
    assert not x > m


def test_bool():
    x, y = Uint(0x00, 8), Uint(0x01, 8)
    assert not bool(x)
    assert bool(y)


def test_abs():
    x = Uint(0x01, 8)
    m = Uint(-1, 8)
    assert abs(x) == 1
    assert abs(m) == 255


def test_add():
    x, y = Uint(0x00, 8), Uint(0x1, 8)
    full = Uint(0xff, 8)
    assert (x + 39).raw == 39
    assert (x + y).raw == 1
    assert (full + 1).raw == 0


def test_and():
    x, y, z = Uint(0x5a5a, 16), Uint(0x5a00, 16), Uint(0x005a, 16)
    i = 0x0a50
    assert (x & y).raw == 0x5a00
    assert (x & z).raw == 0x005a
    assert (x & i).raw == 0x0a50


def test_floordiv():
    x, y = Uint(39, 8), Uint(13, 8)
    i = 3
    assert (x // y).raw == 3
    assert (x // i).raw == 13


def test_index():
    x = Uint(39, 8)
    assert int(x) == 39


def test_invert():
    x = Uint(0x005a, 16)
    assert (~x).raw == 0xffa5


def test_lshift():
    x = Uint(0xa005, 16)
    assert (x << 1).raw == 0x400a
    assert (x << 2).raw == 0x8014
    assert (x << 16).raw == 0


def test_mod():
    x, y = Uint(39, 8), Uint(10, 8)
    assert (x % y).raw == 9
    assert (x % 10).raw == 9


def test_mul():
    m, k = Uint(3, 8), Uint(13, 8)
    assert (m * k).raw == 39
    assert (m * 13).raw == 39


def test_matmul():
    x, y = Uint(0, 8), Uint(1, 8)
    with pytest.raises(TypeError):
        x @ y


def test_neg():
    x = Uint(0x5a, 8)
    assert (-x).raw == 0xa6


def test_or():
    x, y, z = Uint(0x0000, 16), Uint(0x5a00, 16), Uint(0x005a, 16)
    i = 0x0a50
    assert (x | y).raw == 0x5a00
    assert (x | z).raw == 0x005a
    assert (y | i).raw == 0x5a50


def test_pos():
    x = Uint(0xff, 8)
    assert (+x).raw == 0xff


def test_pow():
    x, y = Uint(0x05, 8), Uint(0x05, 8)
    assert (x ** y).raw == 53


def test_rshift():
    x = Uint(0xa005, 16)
    assert (x >> 1).raw == 0x5002
    assert (x >> 2).raw == 0x2801
    assert (x >> 16).raw == 0


def test_sub():
    x, y = Uint(0xff, 8), Uint(0x0f, 8)
    i = 15
    assert (x - y).raw == 0xf0
    assert (x - i).raw == 0xf0


def test_truediv():
    x, y = Uint(0, 8), Uint(1, 8)
    with pytest.raises(TypeError):
        x / y


def test_xor():
    x, y, z = Uint(0x0000, 16), Uint(0x5a00, 16), Uint(0x005a, 16)
    i = 0x0a50
    assert (x ^ y).raw == 0x5a00
    assert (x ^ z).raw == 0x005a
    assert (y ^ i).raw == 0x5050


def test_misc_magics():
    u = Uint(0xff, 8)
    assert str(u) == '<uint8, value=255>'
    assert f'{u:08b}' == '11111111'
