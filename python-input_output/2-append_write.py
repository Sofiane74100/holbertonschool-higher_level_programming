#!/usr/bin/python3
"""
    appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """returns the number of characters added"""
    file = open(filename, 'a+', encoding="utf-8")
    with file:
        file.write(text)
    return len(text)
