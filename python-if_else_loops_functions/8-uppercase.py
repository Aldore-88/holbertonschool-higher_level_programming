#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ascii_num = ord(i)
        if ascii_num > 96 and ascii_num < 123:
            ascii_num = (ascii_num - 32)  # changing to uppercase
        print("{}".format(chr(ascii_num)), end="")
    print("")
