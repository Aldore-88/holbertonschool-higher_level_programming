#!/usr/bin/python3
def safe_print_list_integers(my_list, x=0):
# my_list = [1, 2, 3, 4, 5]
# my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
# x = 6
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count = count + 1
        print()
        return (count)
    except TypeError:
        return (count)