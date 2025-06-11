#!/usr/bin/python3
"""5. Printing a square"""


class Square:
    """
    Declare Square class
    _size(int) - private attibute
    __init__ initiate square
    """
    def __init__(self, size=0):
        """initialse new square size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
        """print("init running")"""

    @property
    def size(self):
        """getter"""
        """print("getter running")"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter size private??"""
        """print("setter running")"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """area of square"""
        squared = (self.__size ** 2)
        """print("area running")"""
        return squared

    def my_print(self):
        """printing square #"""
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
