#!/usr/bin/python3
"""
Module: for Rectangle class 6-base_geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle subclass created. Argument width and height are
    validated through the integer_validator
    """
    def __init__(self, width, height):
        """
        Privitises the width and height
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """
        Returns the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a description of the rectangle
        """
        return (f"[{type(self).__name__}] {self.__width}/{self.__height}")

    