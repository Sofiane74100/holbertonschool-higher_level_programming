#!/usr/bin/python3
import sys
if __name__ == "__main__":
    number_element = len(sys.argv) - 1

    if number_element == 0:
        print("{} arguments.".format(number_element))

    elif number_element == 1:
        print("{} argument:".format(number_element))

    elif number_element > 1:
        print("{} arguments:".format(number_element))
    index = 0

    for arg in sys.argv:
        if index != 0:
            print("{}: {}".format(index, arg))
        index += 1
