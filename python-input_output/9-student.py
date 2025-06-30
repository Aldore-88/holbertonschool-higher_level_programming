#!/usr/bin/python3
"""9.Student to JSON"""


class Student:
    def __init__(self, first_name: str, last_name: str, age: int):
        """Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Class to dictionary"""
        return self.__dict__
