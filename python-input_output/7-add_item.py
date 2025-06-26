#!/usr/bin/python3
"""7-Load, add, save"""
save_file = __import__('5-save_to_json_file.py').save_to_json_file
load_file = __import__('6-load_from_json_file.py').load_from_json_file

"""
loads the file, if file does not exist then create a new one
appends the input from the commandline to the file
"""
filename = "add_item.json"

new_list = load_file(filename)

new_list."""need argv or somehting"""