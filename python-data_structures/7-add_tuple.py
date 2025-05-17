#!/usr/bin/python3

def tuple_check(input_tuple):
    if len(input_tuple) == 0:
        input_tuple = (0, 0)
    elif len(input_tuple) == 1:
        input_tuple = (input_tuple[0], 0)
    return (input_tuple)

#tuple_a = (1, )
#tuple_b = (2,3)
def add_tuple(tuple_a=(), tuple_b=()):
    list_tuple_a = tuple_check(list(tuple_a))
    #print(list_tuple_a)
    list_tuple_b = tuple_check(list(tuple_b))

    pos1_total = list_tuple_a[0] + list_tuple_b[0]
    pos2_total = list_tuple_a[1] + list_tuple_b[1]

    tuple_total = (pos1_total, pos2_total)
    #print(tuple_total)
    return(tuple_total)

