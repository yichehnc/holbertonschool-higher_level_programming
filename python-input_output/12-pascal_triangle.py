#!/usr/bin/python3
"""Module for function to generate pascal's triangle
"""


def pascal_triangle(n):
    """ A function that will return a list of lists
    integers representing the Pascal's triangle of n

    Args:
        n (int): number of layers

    Returns:
        Representation of the triangle using lists
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
