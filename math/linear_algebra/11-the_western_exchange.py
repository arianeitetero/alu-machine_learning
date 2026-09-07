#!/usr/bin/env python3
"""Transpose NumPy arrays."""
import numpy as np


def np_transpose(matrix):
    """Return a new NumPy array containing the transpose of matrix."""
    return np.array(matrix).transpose().copy()
