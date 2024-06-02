#!/usr/bin/python3
"""
    Write a class Student that defines a student
"""


class Student:
    """class to define student"""
    def __init__(self, first_name, last_name, age):
        """
            Public instance attributes:
                first_name
                last_name
                age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list:
            new_attrs = {}
            for index in attrs:
                if hasattr(self, index):
                    new_attrs[index] = getattr(self, index)
            return new_attrs
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
