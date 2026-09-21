#!/usr/bin/env python3

'''
A function that calculates the derivative of a polynomial.
'''


def poly_derivative(poly):
    '''
    Calculates the derivative of a polynomial.
    '''
    if not isinstance(poly, list):
        return None

    if len(poly) <= 1:
        return [0]

    return [poly[i] * i for i in range(1, len(poly))]