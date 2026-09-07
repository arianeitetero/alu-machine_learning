#!/usr/bin/env python3
"""Add two 2D matrices element-wise."""


def add_matrices2D(mat1, mat2):
    """Return the element-wise sum, or None for different shapes."""
    if len(mat1) != len(mat2):
        return None
    if mat1 and len(mat1[0]) != len(mat2[0]):
        return None
    return [[left + right for left, right in zip(row1, row2)]
            for row1, row2 in zip(mat1, mat2)]
