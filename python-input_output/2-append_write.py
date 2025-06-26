#!/usr/bin/python3
"""2.Append to a file"""


def append_write(filename="", text=""):
    """
    Append to a file
    return file with appended text
    """
    with open(filename, "a") as file:
        return file.write(text)