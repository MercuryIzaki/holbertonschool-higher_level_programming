#!/usr/bin/python3
"""
Module 4-from_json_string
Contains function that returns an object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string
    Args:
        my_str (str): JSON string to be converted
    Returns:
        Python object
    """
    return json.loads(my_str)
