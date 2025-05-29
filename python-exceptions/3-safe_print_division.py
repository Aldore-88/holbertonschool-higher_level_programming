#!/usr/bin/python3
def safe_print_division(a, b):
    # a = 12
    # b = 0
    try:
        total = a / b
    except ZeroDivisionError:
        total = None
    finally:
        print("Inside result:{}".format(total))
        return (total)
