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
        Creating a Rectangle instance with five arguments
        succeeds with width set to the first argument,
        height set to the second argument, x set to the
        third argument, y to the fourth argument and id
        set to the fifth argument
        """
        rectangle_1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle_1.width, 1)
        self.assertEqual(rectangle_1.height, 2)
        self.assertEqual(rectangle_1.x, 3)
        self.assertEqual(rectangle_1.y, 4)
        self.assertEqual(rectangle_1.id, 5)

    def test_rectangle_missing_arguments(self):
            """
            Test for missing arguments
            """
            rectangle_1 = Rectangle(1, 2, 3)
            self.assertEqual(rectangle_1.width, 1)
            self.assertEqual(rectangle_1.height, 2)
            self.assertEqual(rectangle_1.x, 3)
            self.assertEqual(rectangle_1.y, 0)

    def test_rectangle_adding_arguments(self):
            """
            Test for modifying and adding arguments after initialization
            """
            rectangle_1 = Rectangle(1, 2, 3)
            self.assertEqual(rectangle_1.width, 1)
            self.assertEqual(rectangle_1.height, 2)
            self.assertEqual(rectangle_1.x, 3)
            self.assertEqual(rectangle_1.y, 0)
            rectangle_1.y = 4
            rectangle_1.id = 5
            self.assertEqual(rectangle_1.y, 4)
            self.assertEqual(rectangle_1.id, 5)

    def test_rectangle_negative(self):
            """
            Test for negative integer arguments
            """
            with self.assertRaises(ValueError):
                rectangle = Rectangle(-1, 2, 3, 4)
            with self.assertRaises(ValueError):
                rectangle = Rectangle(1, -2, 3, 4)
            with self.assertRaises(ValueError):
                rectangle = Rectangle(1, 2, -3, 4)
            with self.assertRaises(ValueError):
                rectangle = Rectangle(1, 2, 3, -4)

    def test_rectangle_zero(self):
            """
            Test for argument is 0
            """
            with self.assertRaises(ValueError):
                rectangle = Rectangle(0, 2, 3, 4)
            with self.assertRaises(ValueError):
                rectangle = Rectangle(1, 0, 3, 4)

    def test_rectangle_area(self):
            """
            Test for correct area calculation
            """
            rectangle_1 = Rectangle(1, 2)
            self.assertEqual(rectangle_1.area(), 2)

    def test_rectangle_display(self):
            """
            Test for correct rectangle display with x
            """
            rectangle_1 = Rectangle(2, 2, 1)
            display_1 = " ##\n ##\n"
            captured_output = StringIO()
            sys.stdout = captured_output
            rectangle_1.display()
            sys.stdout = sys.__stdout__
            self.assertEqual(captured_output.getvalue(), display_1)

    def test_rectangle_display_x(self):
        """
        Test for correct rectangle display with x
        """
        rectangle_1 = Rectangle(2, 2, 1)
        display_1 = " ##\n ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        rectangle_1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), display_1)

    def test_rectangle_display_x_and_y(self):
        """
        Test for correct rectangle display with x and y
        """
        rectangle_1 = Rectangle(2, 2, 1, 1)
        display_1 = "\n ##\n ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        rectangle_1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), display_1)

    def test_rectangle_str_representation(self):
        """
        Test for correct srting representation
        """
        rectangle_1 = Rectangle(1, 2, 3, 4, 99)
        output_1 = "[Rectangle] (99) 3/4 - 1/2"
        self.assertEqual(str(rectangle_1), output_1)

    def test_rectangle_update(self):
        """
        Test for correct update arguments
        """
        rectangle_1 = Rectangle(1, 2, 3, 4, 5)
        rectangle_1.update(6)
        self.assertEqual(rectangle_1.id, 6)

    def test_rectangle_dictionary(self):
        """
        Test for correct dictionary representation
        """
        rectangle_1 = Rectangle(1, 2, 3, 4, 5)
        output_1 = {'width': 1, 'height': 2, 'x': 3, 'y': 4, 'id': 5}
        self.assertEqual(rectangle_1.to_dictionary(), output_1)

    def test_rectangle_create(self):
        """
        Test for correct rectangle instance creation
        """
        rectangle = Rectangle.create(**{ 'height': 2})
        self.assertEqual(rectangle.height, 2)

    def test_rectangle_save_to_file_empty(self):
        """
        Test for a rectangle save to file where read file contents are empty
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r') as f:
             rectangle_1 = f.read()
        self.assertEqual(rectangle_1, '[]')
        os.remove("Rectangle.json")

    def test_rectangle_save_to_file_none(self):
        """
        Test for a rectangle save to file where read file contents are None
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            rectangle_1 = f.read()
        self.assertEqual(rectangle_1, '[]')
        os.remove("Rectangle.json")

    def test_rectangle_load(self):
        """
        Test for loading of file and expected rectangle return
        """
        rectangle_1 = Rectangle(1, 2, 3, 4, 5)
        output_1 = '[Rectangle] (5) 3/4 - 1/2'
        list_rectangle_1_input = [rectangle_1]
        Rectangle.save_to_file(list_rectangle_1_input)
        list_rectangle_1_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangle_1_output[0]), output_1)
        os.remove("Rectangle.json")