#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

"""1.Shapes, Interfaces, and Duck Typing"""


class Shape:
    """Shape abstrace class method"""
    @abstractmethod
    def area(self):
        """abstract method for subclasses area"""
        pass

    @abstractmethod
    def perimeter(self):
        """abstract method for subclasses perimeter"""
        pass


class Circle(Shape):
    """class circle inherited from shape"""
    def __init__(self, radius=0):
        """
        initialize a circle with input radius

        args:
            radius
        """
        self.radius = abs(radius)

    def area(self):
        """
        calculation of area of the circle

        return:
            area of the circle
        """
        area = math.pi * self.radius ** 2
        return area

    def perimeter(self):
        """
        calculation of perimeter of a circle

        return:
            perimeter of the circle
        """
        perimeter = math.pi * 2 * self.radius
        return perimeter


class Rectangle(Shape):
    """class Rectangle inherited from Shape"""
    def __init__(self, width=0, height=0):
        """
        initialize the rectangle class

        args:
            width, height
        """
        self.width = width
        self.height = height

    def area(self):
        """calculation of the area of rectangle"""
        area = self.width * self.height
        return area

    def perimeter(self):
        """calculation of the perimeter of the rectangle"""
        perimeter = 2 * (self.width + self.height)
        return perimeter


def shape_info(shape_name):
    """
    method shape_info - print area and perimeter of shape
    shape_name the object created
    """
    print(f"Area: {shape_name.area()}")
    print(f"Perimeter: {shape_name.perimeter()}")

