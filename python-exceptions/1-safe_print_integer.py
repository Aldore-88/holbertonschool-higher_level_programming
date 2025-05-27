#!/usr/bin/python3
def safe_print_integer(value):
#has_been_print = safe_print_integer(value)
#if not has_been_print:
#    print("{} is not an integer".format(value))
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

