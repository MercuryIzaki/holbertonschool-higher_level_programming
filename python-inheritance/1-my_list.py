#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList that inherits from list.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    """
    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        Assumes all elements of the list are integers.
        """
        print(sorted(self))
