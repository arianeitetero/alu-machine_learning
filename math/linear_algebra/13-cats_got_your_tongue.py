#!/usr/bin/env python3
"""Concatenate NumPy arrays along a selected axis."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Return a new NumPy array concatenating mat1 and mat2."""
    return np.concatenate((mat1, mat2), axis=axis)
