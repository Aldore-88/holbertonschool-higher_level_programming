#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i=0
    try:
        for i in range (x):
            print(my_list[i], end="")
            i += 1
    except IndexError:
        pass
    print()
    return i


"""
def safe_print_list(my_list=[], x=0):
    # my_list = [1, 2, 3, 4, 5]
    # x = 7
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count = count + 1
    except IndexError:
        print()
        return (count)
    else:
        print()
        return (count)
"""