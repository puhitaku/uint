from uint import Uint, Int


def test_and():
    x, y = Uint(0xffff, 16), Int(0x805a, 16)
    assert (x & y).raw == 32858
    assert (y & x).raw == -32678
    assert (x & y).native == 0x805a
    assert (y & x).native == 0x805a


def test_rshift():
    p, m = Int(0x7f, 8), Int(0x8f, 8)
    assert (p >> 2).native == 0x1f
    assert (m >> 2).native == 0xe3


def test_neg():
    x = Int(0x01, 8)
    assert x.raw == 1
    assert x.native == 0x01

    x = -x
    assert x.raw == -1
    assert x.native == 0xff
