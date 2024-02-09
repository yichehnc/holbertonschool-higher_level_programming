#!/usr/bin/python3
"""
Module: Module for class 10-Square
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    "class Square which inherits Rectangle"

    def __init__(self, size):
        """initialization method for a Square instance"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates and returns the area of a square"""
        return self.__size * self.__size
