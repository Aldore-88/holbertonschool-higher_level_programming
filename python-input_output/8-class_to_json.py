#!/usr/bin/python3
"""8.Class to JSON"""


def class_to_json(obj):
    """function returning dict of class"""
    return obj.__dict__
