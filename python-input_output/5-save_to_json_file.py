#!/usr/bin/python3
"""5.Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes object to a text file using json
    needed to input straight to the file.write function
    dump(s) the s returns a string
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
