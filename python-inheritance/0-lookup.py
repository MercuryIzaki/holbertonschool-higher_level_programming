#!/usr/bin/python3
"""
Module 0-lookup
Provides a function that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    Args:
        obj: The object to inspect.
    Returns:
        List of strings.
    """
    return dir(obj)
