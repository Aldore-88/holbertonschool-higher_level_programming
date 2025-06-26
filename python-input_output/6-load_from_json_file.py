#!/usr/bin/python3
"""6.Create object from a JSON file"""
import json


def load_from_json_file(filename):
    with open(filename, "r") as file:
        """reading file"""
        read_data = file.read()

        """making object and return"""
        return json.loads(read_data)
