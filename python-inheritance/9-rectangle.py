#!/usr/bin/python3
"""
Module 9-rectangle
Contains class Rectangle that inherits from BaseGeometry (task 7)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        Constructor for Rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
            The area (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle
        Format: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
