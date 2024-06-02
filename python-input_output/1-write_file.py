#!/usr/bin/python3
"""
     function that writes a string to a text file (UTF8)
     returns the number of characters written
"""


def write_file(filename="", text=""):
    """
        filename is the name of the file
        text is the caractere characters written
    """
    file = open(filename, 'w', encoding="utf-8")
    with file:
        file.write(text)
        return len(text)
