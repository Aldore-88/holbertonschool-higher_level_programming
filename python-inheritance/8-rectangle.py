#!/usr/bin/python3
"""
8.Rectangle
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
