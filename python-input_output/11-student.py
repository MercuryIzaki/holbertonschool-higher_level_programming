#!/usr/bin/python3
"""
Module 11-student
Contains class Student with to_json and reload_from_json
"""


class Student:
    """Class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """
        Initialization of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if isinstance(attrs, list):
            if all(isinstance(s, str) for s in attrs):
                res = {}
                for k, v in self.__dict__.items():
                    if k in attrs:
                        res[k] = v
                return res
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        Args:
            json (dict): dictionary with attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
