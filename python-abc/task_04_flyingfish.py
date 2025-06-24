#!/usr/bin/python3
"""4. The Enigmatic FlyingFish - Exploring Multiple Inheritance"""


class Fish:
    """fish class"""
    def swim(self):
        """method swim of fish"""
        print("The fish is swimming")

    def habitat(self):
        """method habititat of fish"""
        print("The fish lives in water")


class Bird:
    """bird class"""
    def fly(self):
        """method fly of bird"""
        print("The bird is flying")

    def habitat(self):
        """method habitat of bird"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """flying fish class"""
    def fly(self):
        """method fly of flyingfish - overriding parent class fly mehtod"""
        print("The flying fish is soaring!")

    def swim(self):
        """method swim of flying fish - overriding parent class swim method"""
        print("The flying fish is swimming!")

    def habitat(self):
        """
        method habitiat of flyingfish -
        overriding parnt classes habitat methods
        """
        print("The flying fish loves both water and the sky!")

    # def __init__(self):
    #     self.habitat()
    #     self.swim()
    #     self.fly()
