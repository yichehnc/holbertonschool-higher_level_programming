#!/usr/bin/python3
""" Module for ``text_indentation`` function"""


def text_indentation(text):
    """
    prints out text passed in as argument.
    It inserts two newline characters after each '.' or '?'

    Args:
        text (string): a text string to print out

    Returns:
        Nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    if not text:
        print()

    idx = 0

    while idx < len(text):
        print(text[idx], end="")
        if (text[idx] in ".?:"):
            print("\n")
            while idx + 1 < len(text) and text[idx + 1] == " ":
                idx += 1
        idx += 1
