#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry
"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as integer and > 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
