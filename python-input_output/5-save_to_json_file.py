#!/usr/bin/python3
"""
    writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
        arguments:
            my_obj and filename
    """
    file = open(filename, 'w', encoding="utf-8")
    with file:
        json.dump(my_obj, file)
