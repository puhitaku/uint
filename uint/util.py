from typing import Union, NewType, Optional
from uint import Uint

Fixed = NewType('RichInt', Union['Uint', 'Int'])


def generate_bitmask(width: int) -> int:
    return (1 << width) - 1


def twocomp(v: Union[Fixed, int], width: Optional[int] = None) -> Union[Fixed, int]:
    if issubclass(type(v), Uint):
        return (-v).native
    elif isinstance(v, int):
        if width is None:
            raise ValueError("width must be specified to calculate two's complimentary of plain int")
        if v < 0:
            v = -v
        return generate_bitmask(width) - v + 1
    else:
        raise TypeError(f"cannot calculate two's complimentary of type {type(v)}")





