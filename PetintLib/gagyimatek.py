"""
Gagyimatek
A négy alapművelet + hatványozás gagyi változata:
Csak össeadással meg kivonással.
"""

__all__ = ['osszead', 'kivon', 'szorzas', 'oszt', 'hatvany']
__version__ = '2.0.3'

"""Műveletek"""


def osszead(a, b):
    """
    A két beadott szám össege
    (a+b)
    """
    return a + b


def kivon(a, b):
    """
    A két beadott szám külombsége
    (a-b)
    """
    return a - b


def szorzas(a, b):
    """
    Összeszoroz két számot, de gagyin
    (a*b)
    """
    _eredmeny = 0
    for x in range(a):
        _eredmeny = osszead(_eredmeny, b)
    return _eredmeny


def oszt(a, b):
    """
    A világ legrosszabb osztómetódusa (a/b)
    """
    if b == 0: raise ZeroDivisionError("Nullahiba")
    _eredmeny = 0
    while a > 0:
        a = kivon(a, b)
        _eredmeny = osszead(_eredmeny, 1)
    return _eredmeny


def hatvany(a, b):
    """
    Az első szám hatványraemelése (a^b)
    """
    if b == 0:
        return 1
    _eredmeny = a
    for x in range(b - 1):
        _eredmeny = szorzas(_eredmeny, a)
    return _eredmeny
