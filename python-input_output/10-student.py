#!/usr/bin/python3
"""10.Student to JSON with filter"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """instantiate instance with first_name, last_name, age attribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """
        retreives the dictionary representation of a Student
        with specified attribute if available
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for attribute in attrs:
            if hasattr(self, attribute):
                new_dict[attribute] = getattr(self, attribute)
        return new_dict
