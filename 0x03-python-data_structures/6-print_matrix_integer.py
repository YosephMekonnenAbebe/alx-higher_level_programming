#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for irow in range(len(matrix)):
        for jcolumn in range(len(matrix[irow])):
            if jcolumn != 0:
                print(" ", end='')
            print("{:d}".format(matrix[irow][jcolumn]), end='')
        print()

