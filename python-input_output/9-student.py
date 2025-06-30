#!/usr/bin/python3
"""9.Student to JSON"""

class Student:
    def __init__(self, first_name, last_name, age):
        """Student class"""
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """Class to dictionary"""
        self.__dict__
