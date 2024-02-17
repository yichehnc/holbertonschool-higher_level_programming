#!/usr/bin/python3
""" Module for rectangle class """


class Rectangle:
    """
       Rectangle class
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        initializes an instance of class with data
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        returns the height of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets value of width.

        Returns:
            Nothing
        """

        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
        type(self).number_of_instances += 1

    @property
    def height(self):
        """
        returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets value of height.

        Returns:
            Nothing
        """

        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            Calculated area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            Calculated perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        prints the rectangle with teh character #
        """
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        for i in range(self.__height):
            if (i > 0):
                result += '\n'
            result += ("#" * self.__width)
        return result

    def __repr__(self):
        """
        return a string representation of the rectangle
        with which we can recreate a new instance by using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print the message `Bye rectangle...`
        when a rectangle instance is deleted
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
