__version__ = '0.0.1'
from random import randint

def randbyte() -> str:
    """Returns a random byte"""
    return hex(randint(0, 255))


def randbytes(bytecount: int) -> list:
    """Returns a given number of bytes"""
    return [randbyte() for _ in range(bytecount)]


def randbytearray(dimx: int, dimy: int):
    """Returns a random byte array of given dimensions"""
    return[bytearray.append(randbytes(dimx)) for _ in range(dimy)]

