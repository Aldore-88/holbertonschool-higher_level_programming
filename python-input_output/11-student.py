#!/usr/bin/python3
"""11.Student to disk and reload"""
class Student:
    def __init__(self, first_name, last_name, age):
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
                """creates a dictionary with attributes and corresponding """
                new_dict[attribute] = getattr(self, attribute)
        return new_dict
    
    def reload_from_json(self, json):
        """assume json is always dictionary"""
