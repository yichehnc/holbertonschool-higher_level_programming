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
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square
        object that can be used to create a normal square
        """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """
        Assign a key/value arguments to attributes
        """

        for i, value in enumerate(args):
            if i == 0:
                self.id = value
            elif i == 1:
                self.size = value
            elif i == 2:
                self.x = value
            elif i == 3:
                self.y = value

        for key, value in kwargs.items():
            # key in dictionary is a string
            if key == 'id':
                self.id = value
            if key == 'size':
                self.size = value
            if key == 'x':
                self.x = value
            if key == 'y':
                self.y = value

    def to_dictionary(self):
        """
        Returns a dictionary representation of a Square
        """
        # make dictionary from instances
        return {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.size}
