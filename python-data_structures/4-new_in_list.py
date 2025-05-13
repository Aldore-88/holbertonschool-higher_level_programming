#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    new_list[idx] = element

    if idx > len(my_list):
        return (None)
    if idx < 0:
        return (None)
    else:
        return (new_list)
