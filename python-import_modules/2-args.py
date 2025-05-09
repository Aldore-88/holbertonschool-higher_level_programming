#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0: arguments.")
    elif len(sys.argv) > 1:
        if len(sys.argv) == 2:
            print("1 argument:")
        elif len(sys.argv) > 2:
            print(len(sys.argv), end=": arguments:\n")
        for i in range(len(sys.argv)):
            if i > 0:
                print(i, end=": ")
                print(sys.argv[i])
