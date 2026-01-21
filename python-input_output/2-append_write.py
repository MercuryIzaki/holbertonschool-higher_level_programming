#!/usr/bin/python3
"""
Module 2-append_write
Contains function that appends a string to a text file
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    Args:
        filename (str): name of the file
        text (str): text to append
    Returns:
        The number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
