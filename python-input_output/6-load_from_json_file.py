#!/usr/bin/python3
"""
Module 6-load_from_json_file
Contains function that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file"
    Args:
        filename: name of the file to read from
    Returns:
        The Python object represented by the JSON file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
