#!/usr/bin/python3
"""1.Write to a  file"""


def write_file(filename="", text=""):
    """
    write_file "filename" with "text"
    return the file with overwritten text
    """
    with open(filename, "w") as file:
        return file.write(text)
