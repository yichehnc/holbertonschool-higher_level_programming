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

    def test_to_json_string_none(self):
        """
        Test to_json_string with None as argument
        """
        str = Base.to_json_string(None)
        self.assertEqual(str, "[]")

    def test_to_json_string_empty_list(self):
        """
        Test to_json_string with empty list argument
        """
        str = Base.to_json_string([])
        self.assertEqual(str, "[]")

    def test_to_json_string_non_empty_list(self):
        """
        Test to_json_string with non empty list argument
        """
        str = Base.to_json_string([{"id": 10}])
        self.assertEqual(str, "[{\"id\": 10}]")

    def test_from_json_string_empty_list(self):
        """Testing from_json_string with empty list string"""
        lst = Base.from_json_string("[]")
        self.assertEqual(lst, [])

    def test_from_json_string_list_with_content(self):
        """Testing from_json_string with list with content"""
        lst = Base.from_json_string("[{\"id\": 10}]")
        self.assertEqual(lst, [{"id": 10}])