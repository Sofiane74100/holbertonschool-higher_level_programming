#!/usr/bin/python3
"""
    Write a function that returns
    True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj (_type_): _description_
        a_class (_type_): _description_

    Returns:
        _type_: _description_
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
