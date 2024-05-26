#!/usr/bin/python3
"""
    prints a text with 2 new lines after each of these characters: ., ? and :
    one argument: text
    text must be a string
"""


def text_indentation(text):
    """
        prints a text with 2 new lines after each othese characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    my_list = [".", "?", ":"]
    for index in text:
        if index in my_list:
            print(index + "\n\n", end="")
        else:
            print(f"{index}", end="")
