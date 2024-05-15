#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line_matrice in matrix:
        for number in line_matrice:
            if number == line_matrice[-1]:
                print("{:d}".format(number), end="")
            else:
                print("{:d} ".format(number), end="")
        print()
