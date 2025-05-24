#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary.items())
    #print(sorted_dictionary)
    for key, value in sorted_dictionary:
        print("{}: {}".format(key, value))