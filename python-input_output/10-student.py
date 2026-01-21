#!/usr/bin/python3
"""
Module 10-student
Contains class Student that defines a student with disk filter
"""


class Student:
    """Class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """
        Initialization of the student
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attributes in the list are retrieved
        """
        if (isinstance(attrs, list) and
                all(isinstance(s, str) for s in attrs)):
            res = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    res[k] = v
            return res
        return self.__dict__
