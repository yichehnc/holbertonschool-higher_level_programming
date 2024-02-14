#!/usr/bin/python3
"""
Module - square.py
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        class Square constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Size inherits from Rectangle
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Size value validation inherits from Rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square
        object that can be used to create a normal square
        """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))
