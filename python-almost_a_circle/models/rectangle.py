#!/usr/bin/python3
"""
Module - rectangle.py
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class Rectangle constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Retrieves itself
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Determines whether the value is suitable for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves itself
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Determines whether the value is suitable for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Retrieves itself
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Determines whether the value is suitable for x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Retrieves itself
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Determines whether the value is suitable for y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        Prints the rectangle with #
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for i in range(self.x):
                print(' ', end='')
            for i in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """
        Returns a string representation of the rectangle
        object that can be used to create a normal rectangle
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        Assign a key/value arguments to attributes
        """

        for i, value in enumerate(args):
            if i == 0:
                self.id = value
            elif i == 1:
                self.width = value
            elif i == 2:
                self.height = value
            elif i == 3:
                self.x = value
            else:
                self.y = value

        for key, value in kwargs.items():
            # print (kwargs)
            # key in dictionary is a string
            if key == 'id':
                self.id = value
            if key == 'width':
                self.width = value
            if key == 'height':
                self.height = value
            if key == 'x':
                self.x = value
            if key == 'y':
                self.y = value

    def to_dictionary(self):
        """
        Returns a dictionary representation of a Rectangle
        """
        # make dictionary from instances
        return {'id': self.id, 'x': self.x, 'y': self.y,
                'height': self.height, 'width': self.width}
