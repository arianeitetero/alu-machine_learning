#!/usr/bin/env python3
"""Transpose 2D matrices represented by nested lists."""


def matrix_transpose(matrix):
    """Return a new matrix containing the transpose of matrix."""
    return [[row[column] for row in matrix] for column in range(len(matrix[0]))]
