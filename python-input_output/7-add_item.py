#!/usr/bin/python3
"""7-Load, add, save"""
from sys import argv

save_file = __import__("5-save_to_json_file").save_to_json_file
load_file = __import__("6-load_from_json_file").load_from_json_file

"""
loads the file, if file does not exist then create a new one
appends the input from the commandline to the file
"""
filename = "add_item.json"

try:
    new_list = load_file(filename)
except FileNotFoundError:
    new_list = []

new_list.extend(argv[1:])
save_file(new_list, filename)