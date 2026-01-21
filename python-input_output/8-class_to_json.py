#!/usr/bin/python3
"""
Module 8-class_to_json
Contains function that returns the dictionary description of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object
    Args:
        obj: an instance of a Class
    Returns:
        dictionary representation of the object
    """
    return obj.__dict__
