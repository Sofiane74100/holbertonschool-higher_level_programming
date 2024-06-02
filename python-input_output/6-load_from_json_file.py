#!/usr/bin/python3
"""
    Write a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Args:
        filename
    """
    file = open(filename, 'r', encoding="utf-8")
    with file:
        object = json.load(file)
    return object
