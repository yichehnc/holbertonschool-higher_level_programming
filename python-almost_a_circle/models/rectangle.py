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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Retrieves itself
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Determines whether the value is suitable for width
        """
        self.__width = width

    @property
    def height(self):
        """
        Retrieves itself
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Determines whether the value is suitable for height
        """
        self.__height = height

    @property
    def x(self):
        """
        Retrieves itself
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Determines whether the value is suitable for x
        """
        self.__x = x

    @property
    def y(self):
        """
        Retrieves itself
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Determines whether the value is suitable for y
        """
        self.__y = y
