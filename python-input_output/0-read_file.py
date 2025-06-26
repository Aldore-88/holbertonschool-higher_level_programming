#!/usr/bin/python3
"""0.Read file"""

def read_file(filename=""):
    """
    need to use with method
    -> with takes care of closing files
    """

    with open(filename) as file:
        print(file.read(), end="")

    # f = open(filename)
    # print(f.read())
