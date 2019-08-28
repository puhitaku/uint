from typing import Union, NewType, Optional

Fixed = NewType('RichInt', Union['Uint', 'Int'])


def generate_bitmask(width: int) -> int:
    return (1 << width) - 1


def twocomp(v, width: Optional[int] = None):
    if hasattr(v, 'native'):  # Uint or Int
        return (-v).native
    elif isinstance(v, int):
        if width is None:
            raise ValueError("width must be specified to calculate two's complimentary of plain int")
        if v < 0:
            v = -v
        return generate_bitmask(width) - v + 1
    else:
        raise TypeError(f"cannot calculate two's complimentary of type {type(v)}")


def is_twocomp(v, bits):
    return bool(v & (1 << (bits - 1)))
