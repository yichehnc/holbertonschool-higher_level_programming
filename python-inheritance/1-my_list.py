#!/usr/bin/python3
"""
Module: Writing a class MyList that inherits from list
"""


class MyList(list):
    """
    print_sorted(self): Prints a sorted list
    """
    def print_sorted(self):
        """
        Sorts a list and prints a list
        """
        sorted_list = sorted(self)
        print(sorted_list)
