#!/usr/bin/python3
"""
9.Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class rectangle that inherits base geometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        return self.__width * self.__height
