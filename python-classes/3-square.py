#!/usr/bin/python3
"""
Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a
TypeError exception with the message size must be an integer

if size is less than 0, raise a ValueError
exception with the message size must be >= 0

Public instance method: def area(self): that returns the current square area
"""


class Square:
    """
    __init__ initialises square
    area(self) returns __size^2 for area of square
    """

    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__sizeA = size

    def area(self):
        squared = (self.__sizeA ** 2)
        return squared
