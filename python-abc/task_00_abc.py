#!/usr/bin/python3
from abc import ABC, abstractmethod
"""0. Abstract Animal Class and its Subclassses"""


class Animal:
    """Abstract base class for animals"""
    @abstractmethod
    def sound(self):
        """abstract method for sound (checks for this in child methods?)"""
        pass


class Dog(Animal):
    """dog class inheriting base class animal"""
    def sound(self):
        """return sound of a dog"""
        return ("Bark")


class Cat(Animal):
    """cat class inheriting base class animal"""
    def sound(self):
        """return sound of a cat"""
        return ("Meow")
