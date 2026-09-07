#!/usr/bin/env python3
"""Perform element-wise NumPy operations."""
import numpy as np


def np_elementwise(mat1, mat2):
    """Return the sum, difference, product, and quotient of two arrays."""
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
