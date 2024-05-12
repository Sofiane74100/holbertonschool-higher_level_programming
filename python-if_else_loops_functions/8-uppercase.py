#!/usr/bin/python3
def uppercase(str):
    for Alpha_upper in str:
        if ord(Alpha_upper) >= 97 and ord(Alpha_upper) <= 122:
            Alpha_upper = chr(ord(Alpha_upper) - 32)

        print("{}".format(Alpha_upper), end="")
    print("")
