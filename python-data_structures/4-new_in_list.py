#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    new_list[idx] = element

    if idx > len(my_list):
        return (my_list)
    if idx < 0:
        return (my_list)
    else:
        return (new_list)
