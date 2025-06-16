#!/usr/bin/python3
"""
!!!!#### NEED TO MAKE A TEST FILE FOR THIS!!!
"""
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError("{} must be an integer".format(e.__class__.__name__))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(e.__class__.__name__))