#!/usr/bin/python3
Square = __import__('4-square').Square
print("part 1")
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

print("part 2")
my_square.size = 33
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

print("part 3")
try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)