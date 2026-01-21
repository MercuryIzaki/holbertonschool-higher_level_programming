#!/usr/bin/python3
"""
This module contains a class MyList.
MyList inherits from the built-in list class.
"""


class MyList(list):
    """
    MyList class that provides extra list functionality.
    It inherits from the standard list.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.
        All elements are assumed to be of type int.
        Does not modify the original list.
        """
        print(sorted(self))
