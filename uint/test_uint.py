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


def test_minus():
    pass
    #u = Uint(0x)
