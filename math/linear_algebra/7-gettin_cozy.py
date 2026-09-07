#!/usr/bin/env python3
"""Concatenate two 2D matrices along a selected axis."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Return a new concatenated matrix, or None if shapes are incompatible."""
    if axis == 0:
        if mat1 and mat2 and len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1 + mat2]
    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1[:] + row2[:] for row1, row2 in zip(mat1, mat2)]
    return None
