#!/usr/bin/python3
import sys
if __name__ == "__main__":
    number_element = len(sys.argv) - 1
    result = 0
    index = 0
    for arg in sys.argv:
        if index != 0:
            result += int(arg)
        index += 1
    print("{}".format(result))
