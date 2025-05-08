#!/usr/bin/python3
for tens_digit in range(0, 10):
    for ones_digit in range(0, 10):
        total = tens_digit * 10 + ones_digit
        if (tens_digit < ones_digit):
            print("{:02d}".format(total))
