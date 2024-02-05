#!/usr/bin/python3
"""A module with one function say_my_name"""


def say_my_name(first_name, last_name=""):
    """Prints <first_name> <last_name>

        Args:
            first_name (string): the first name
            last_name (string): the last name

        Returns:
            Nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
