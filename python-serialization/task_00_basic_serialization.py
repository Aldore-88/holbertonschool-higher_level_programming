#!/usr/bin/python3
"""0.Basic Serialization"""
import json

def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    """
    data - python dictionary with data
    filename - output JSON file

    writes to the file as a json
    """
    with open(filename, "w") as file:
        return json.dump(data, file)

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    """
    return the read the file as a json file
    """
    with open(filename, "r") as file:
        return (json.load(file))
