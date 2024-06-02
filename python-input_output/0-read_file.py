#!/usr/bin/python3
"""
    function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
        Args:filename (str, optional): _description_. Defaults to "".
    """
    file = open(filename, 'r', encoding="utf-8")
    with file:
        print(file.read(), end='')
