#!/usr/bin/python3
"""
Unittest for Square module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
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