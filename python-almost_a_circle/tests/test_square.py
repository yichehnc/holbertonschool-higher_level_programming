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

    def test_square_area(self):
        """
        Test for correct area calculation
        """
        square_1 = Square(2)
        self.assertEqual(square_1.area(), 4)

    def test_square_display(self):
        """
        Test for correct Square display
        """
        square_1 = Square(2)
        display_1 = "##\n##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        square_1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), display_1)

    def test_square_display_x(self):
        """
        Test for correct Square display with x
        """
        square_1 = Square(2, 1)
        display_1 = " ##\n ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        square_1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), display_1)

    def test_square_display_x_and_y(self):
        """
        Test for correct Square display with x and y offset
        """
        square_1 = Square(2, 1, 1)
        display_1 = "\n ##\n ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        square_1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), display_1)

    def test_square_str_representation(self):
        """
        Test for correct string representation
        """
        square_1 = Square(1, 2, 3, 4)
        output_1 = "[Square] (4) 2/3 - 1"
        self.assertEqual(str(square_1), output_1)

    def test_square_update(self):
        """
        Test for correct update arguments
        """
        square_1 = Square(1, 2, 3, 4)
        square_1.update(5)
        self.assertEqual(square_1.id, 5)

    def test_square_dictionary(self):
        """
        Test for correct dictionary representation
        """
        square_1 = Square(1, 2, 3, 4)
        output_1 = {'size': 1, 'x': 2, 'y': 3, 'id': 4}
        self.assertEqual(square_1.to_dictionary(), output_1)

    def test_square_create(self):
        """
        Test for correct Square instance creation
        """
        square_1 = Square.create(**{ 'size': 2 })
        self.assertEqual(square_1.size, 2)

    def test_square_save_to_file(self):
        """
        Test for a Square save to file where read file contents are empty
        """
        filename = "Square.json"
        if (os.path.isfile(filename)):
            os.remove(filename)

        Square.save_to_file(None)
        content = ""
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        os.remove(filename)
        self.assertEqual(content, "[]")

        Square.save_to_file([])
        content = ""
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        os.remove(filename)
        self.assertEqual(content, "[]")


    def test_square_load(self):
        """
        Test for loading of file and expected Square return
        """
        square_1 = Square(1, 2, 3, 4)
        output_1 = '[Square] (4) 2/3 - 1'
        list_square_1_input = [square_1]
        Square.save_to_file(list_square_1_input)
        list_square_1_output = Square.load_from_file()
        self.assertEqual(str(list_square_1_output[0]), output_1)
        os.remove("Square.json")