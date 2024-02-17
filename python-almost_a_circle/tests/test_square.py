#!/usr/bin/python3
"""
Unittest for Square module
"""
import unittest
from models.base import Base
from models.square import square
from models.square import Square
from io import StringIO
import io
import sys
import os


class TestSquare(unittest.TestCase):
    """
    Tests for Square Class
    """
    def test_square_correct_arguments(self):
        """
        Test for correct input
        """
        square_1 = Square(1, 2, 3, 4)
        self.assertEqual(square_1.size, 1)
        self.assertEqual(square_1.x, 2)
        self.assertEqual(square_1.y, 3)
        self.assertEqual(square_1.id, 4)
        
    def test_square_missing_arguments(self):
            """
            Test for missing arguments
            """
            square_1 = Square(1, 2)
            self.assertEqual(square_1.size, 1)
            self.assertEqual(square_1.x, 2)
            self.assertEqual(square_1.y, 0)

    def test_square_adding_arguments(self):
            """
            Test for modifying and adding arguments after initialization
            """
            square_1 = Square(1, 2)
            self.assertEqual(square_1.size, 1)
            self.assertEqual(square_1.x, 2)
            self.assertEqual(square_1.y, 0)
            square_1.y = 3
            square_1.id = 4
            self.assertEqual(square_1.y, 3)
            self.assertEqual(square_1.id, 4)

    def test_square_negative(self):
            """
            Test for negative integer arguments
            """
            with self.assertRaises(ValueError):
                square_1 = Square(-1, 2, 3)
            with self.assertRaises(ValueError):
                square_1 = Square(1, -2, 3)
            with self.assertRaises(ValueError):
                square_1 = Square(1, 2, -3)

    def test_square_string(self):
        """
        Test for string arguments
        """
        with self.assertRaises(TypeError):
            square_1 = Square("1", 2, 3)
        with self.assertRaises(TypeError):
            square_1 = Square(1, "2", 3)
        with self.assertRaises(TypeError):
            square_1 = Square(1, 2, "3")

    def test_square_zero(self):
            """
            Test for argument is 0
            """
            with self.assertRaises(ValueError):
                square_1 = Square(0, 2)
