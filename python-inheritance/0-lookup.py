#!/usr/bin/python3
"""
This module provides a function called lookup.
The function returns a list of attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to be inspected.

    Returns:
        A list of strings representing attributes and methods.
    """
    return dir(obj)
