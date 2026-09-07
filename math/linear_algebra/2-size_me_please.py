#!/usr/bin/env python3
"""Calculate the shape of a matrix represented by nested lists."""


def matrix_shape(matrix):
    """Return the dimensions of a nested list as a list of integers."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) == 0:
            break
        matrix = matrix[0]
    return shape
