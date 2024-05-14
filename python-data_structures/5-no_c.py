#!/usr/bin/python3
def no_c(my_string):
    characters = "cC"
    translation_table = str.maketrans("", "", characters)
    my_string = my_string.translate(translation_table)
    return my_string
