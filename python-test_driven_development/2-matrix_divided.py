#!/usr/bin/python3
"""
This module contains function matrix_divided for dividing
all elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all the elements in a matrix

    Args:
        matrix (array): a two dimensional matrix of integers or floats
        div (int): the divisor

    Return:
        array: an array with same dimension as matrix, with each element
        divided by the divisor
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    is_list_of_lists = all([isinstance(row, list) for row in matrix])
    rows_equal = all([len(row) == len(matrix[0]) for row in matrix])
    matrix_values_valid = (all([
        (isinstance(item, int) or isinstance(item, float))
        for row in matrix for item in row]))

    if not (is_list_of_lists and matrix_values_valid):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    if not rows_equal:
        raise TypeError(
            "Each row of the matrix must have the same size"
            )

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item/div, 2) for item in row] for row in matrix]
