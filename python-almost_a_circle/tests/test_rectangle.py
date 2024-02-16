#!/usr/bin/python3
"""
Unittest for Rectangle module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import io
import sys
import os


class TestRectangle(unittest.TestCase):
    """
    Tests for Rectangle Class
    """
    def test_rectangle_only(self):
        """
        Test for correct input
        """
        rectangle_1 = Rectangle(1, 2)
        self.assertEqual(rectangle_1.width, 1)
        self.assertEqual(rectangle_1.height, 2)

    def test_rectangle_correct_arguments(self):
        """
        Test for correct input
        """
        rectangle_1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle_1.width, 1)
        self.assertEqual(rectangle_1.height, 2)
        self.assertEqual(rectangle_1.x, 3)
        self.assertEqual(rectangle_1.y, 4)
        self.assertEqual(rectangle_1.id, 5)