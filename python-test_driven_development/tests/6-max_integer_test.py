#!/usr/bin/python
"""Unit tests for `max_integer`"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_at_start(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)

    def test_all_negative_list(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_list_with_one_value(self):
        self.assertEqual(max_integer([10]), 10)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()
