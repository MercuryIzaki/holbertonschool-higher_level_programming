#!/usr/bin/python3
"""
Module 10-square
Contains class Square that inherits from Rectangle (task 9)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size):
        """
        Constructor for Square
        Args:
            size (int): side length of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
