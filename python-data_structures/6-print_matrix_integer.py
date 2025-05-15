#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = 0
    while row < len(matrix):
        col = 0
        while col < len(matrix[row]):
            if col != 0:
                print("", end=" ")
            print(matrix[row][col], end="")
            col = col + 1
        print()
        row = row + 1
