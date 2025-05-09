#!/usr/bin/python3
if __name__ == "__main__":
    import sys

len = len(sys.argv)
total = 0

for i in range(len):
    if i >= 1:
        total = total + int(sys.argv[i])
print(total)
