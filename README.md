# uint [![CI](https://travis-ci.org/puhitaku/uint.svg?branch=master)](https://travis-ci.org/puhitaku/uint) [![Coverage Status](https://coveralls.io/repos/github/puhitaku/uint/badge.svg?branch=master)](https://coveralls.io/github/puhitaku/uint?branch=master)

*Fixed-width integer and calculation for Python*

```
$ pip install uint
```


## Fixed-width integers for Python

uint provides two classes: `Uint` and `Int`. They are calculated like `int` but is fixed-width so they behave like ones that you're familiar with ... like in C language.

```
In [1]: from uint import Uint, Int

In [2]: u, i = Uint(0xff, 8), Int(0xff, 8)

In [3]: u
Out[3]: <uint8, value=255>

In [4]: i
Out[4]: <int8, value=-1>

In [5]: u << 2 >> 1
Out[5]: <uint8, value=126>

In [6]: i << 2 >> 1
Out[6]: <int8, value=-2>
```


Of course they overflows when you do like:

```
In [1]: from uint import Uint, Int

In [2]: u, i = Uint(0xff, 8), Int(0x7f, 8)

In [3]: u, i
Out[3]: (<uint8, value=255>, <int8, value=127>)

In [4]: u+1, i+1
Out[4]: (<uint8, value=0>, <int8, value=-128>)
```

## Register with multiple fields inside

The original purpose of this package is to reduce labor of calculating "register values" in several MCUs and SoCs. See `examples` directory for detailed usage.

```
In [1]: from uint import Register

In [2]: reg = Register('reg')

In [3]: reg[15:8] = 'f1'

In [4]: reg[7:0] = 'f2'

In [5]: reg['f1'] = 0x5A

In [6]: reg['f2'] = 0x0F

In [7]: hex(reg.encode())
Out[7]: '0x5a0f'

In [8]: reg.decode(0x1234)

In [9]: reg['f1'].value.wire.hex
Out[9]: "8'h12"

In [10]: reg['f2'].value.wire.hex
Out[10]: "8'h34"
```

