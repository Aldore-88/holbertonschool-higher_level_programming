#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.sizeA = size

    @property
    def size(self):
        sizeB = self.sizeA
        return sizeB

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        squared = (self.sizeA ** 2)
        return squared
