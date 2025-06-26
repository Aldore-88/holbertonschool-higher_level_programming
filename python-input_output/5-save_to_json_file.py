#!/usr/bin/python3
"""5.Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes object to a text file using json
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
