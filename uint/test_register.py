from pytest import raises
from uint import Register


def test_create():
    reg = Register('reg')
    assert reg.name == 'reg'


def test_define_field():
    reg = Register('reg')
    reg[15:8] = 'f1'
    reg[7:0] = 'f2'
    assert [f.name for f in reg.fields] == ['f1', 'f2']

    reg['f1'] = 0b10101010
    assert reg['f1'].name == 'f1'
    assert reg['f1'].index == slice(15, 8)
    assert reg['f1'].value == 0b10101010

    reg['f2'] = 0b01010101
    assert reg['f2'].name == 'f2'
    assert reg['f2'].index == slice(7, 0)
    assert reg['f2'].value == 0b01010101


def test_detect_overlap():
    reg = Register('reg')
    reg[7:0] = 'f1'
    with raises(Register.OverlappedRange):
        reg[15:7] = 'f2'

    with raises(Register.OverlappedRange):
        reg[5] = 'f2'


def test_overlap():
    reg = Register('reg')
    reg[31:16] = 'f1'
    try:
        reg[16:0] = 'f2'
    except Register.OverlappedRange as e:
        assert e.args[0] == '[16:0] overlaps to f1[31:16].'


def test_encode():
    reg = Register('reg')
    reg[15] = 'onebit'
    reg[14:13] = 'twobits'
    reg[12:10] = 'threebits'
    reg[9:8] = 'foo'
    reg[7:0] = 'byte'

    reg['onebit'] = 0b1
    reg['twobits'] = 0b01
    reg['threebits'] = 0b010
    reg['foo'] = 0b11
    reg['byte'] = 0b11110000

    assert reg.encode() == 0b1_01_010_11_11110000


def test_decode():
    reg = Register('reg')
    reg[15:12] = 'fourbits'
    reg[11] = 'onebit'
    reg[10:9] = 'twobit'
    reg[8] = 'foo'
    reg[7:0] = 'byte'

    reg.decode(0b1010_1_10_0_00110101)

    assert reg['fourbits'].value == 0b1010
    assert reg['onebit'].value == 0b1
    assert reg['twobit'].value == 0b10
    assert reg['foo'].value == 0b0
    assert reg['byte'].value == 0b00110101


def test_magics():
    reg = Register('reg')
    reg[15:8] = 'f1'
    reg[7:0] = 'f2'

    assert len(reg) == 16
    assert repr(reg) == '<register "reg">'
