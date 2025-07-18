#!/usr/bin/python3
"""6.Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """loading from json file"""
    with open(filename, "r") as file:
        """reading file and makes it a string"""
        read_data = file.read()

        """making object from the string and return"""
        return json.loads(read_data)
"""come back to laters"""