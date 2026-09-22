#!/usr/bin/env python3

'''
A function that calculates the derivative of a polynomial.
'''


def poly_derivative(poly):
    '''
    Calculates the derivative of a polynomial.
    '''
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    for coefficient in poly:
        if not isinstance(coefficient, (int, float)):
            return None

    if len(poly) == 1:
        return [0]

    derivative = [poly[i] * i for i in range(1, len(poly))]

    if all(coefficient == 0 for coefficient in derivative):
        return [0]

    return derivative