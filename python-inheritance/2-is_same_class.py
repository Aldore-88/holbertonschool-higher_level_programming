#!/usr/bin/python3
"""
2. Exact same object
"""


def is_same_class(obj, a_class):
    """
    checking obj type, and comparing against a_class

    return True if obj is int
    """
    if type(obj) is a_class:
        return True
    else:
        return False
