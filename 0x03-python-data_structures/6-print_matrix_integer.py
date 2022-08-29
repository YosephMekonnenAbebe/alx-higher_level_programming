#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rowi in range(len(matrix)):
        for columnj in range(len(matrix[rowi])):
            if columnj != 0:
                print(" ", end='')
                print("{:d}".format(matrix[rowi][columnj]), end='')
        print()
