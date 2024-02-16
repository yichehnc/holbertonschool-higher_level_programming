#!/usr/bin/python3
"""
Unittest for Base module
"""
import unittest
from models.base import Base
import io
import sys
import os


class TestBase(unittest.TestCase):
    """
    Tests for Base Class
    """
    def test_base_arguments(self):
        """
        Testing for missing arguments
        """
        base_1 = Base()
        self.assertEqual(base_1.id, 1)
        base_1_compare = base_1.id > 0
        self.assertEqual(base_1_compare, True)
        base_2 = Base()
        self.assertEqual(base_1.id + 1, base_2.id)
        base_3 = Base(2)
        self.assertEqual(base_3.id, 2)