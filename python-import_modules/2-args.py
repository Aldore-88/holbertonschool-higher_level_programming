#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("0: arguments.")
elif len(sys.argv) > 1:
    for i in range(len(sys.argv)):
        if i > 0:
            print(i, end=": ")
            print(sys.argv[i])
