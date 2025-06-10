#!/usr/bin/python3

class Square:
    """
    Declare Square class
    
    _size(int) - private attibute
    __init__ initiate square

    """
    def __init__(self, size=0):
        """
        initialse new square
        
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.sizeA = size

    @property
    def size(self):
        """
        getter size
        """
        sizeB = self.sizeA
        return sizeB

    @size.setter
    def size(self, size):
        """
        setter
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """
        area of square
        """
        squared = (self.sizeA ** 2)
        return squared
