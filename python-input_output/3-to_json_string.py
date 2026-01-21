#!/usr/bin/python3
"""
Module 3-to_json_string
Contains function that returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    Args:
        my_obj: object to be serialized
    Returns:
        JSON representation string
    """
    return json.dumps(my_obj)
