#!/usr/bin/python3
"""Interger addition"""


def add_integer(a, b=98):
    """
    Args:
    a float
    b float

    Return:
    Sum of the 2 integers

    Raise:
    TypeError if a or b are non-integers
    """

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    else:
        total = a + b
        return (total)
