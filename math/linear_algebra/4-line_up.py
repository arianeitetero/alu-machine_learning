#!/usr/bin/env python3
"""Add two one-dimensional arrays element-wise."""


def add_arrays(arr1, arr2):
    """Return the element-wise sum, or None for different shapes."""
    if len(arr1) != len(arr2):
        return None
    return [left + right for left, right in zip(arr1, arr2)]
