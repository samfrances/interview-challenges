#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""problemB.py: Prints the numbers from 1 to 100, one per line.  However for
multiples of 3 prints “Kit” instead of the number and for the multiples of
five print “Kat”.  For numbers which are a multiple of both 3 and 5, prints
“KitKat”.

This version does not use any of the division or modulus operators ("/", "//",
or "%"), either directly or indirectly.
"""


def divisible(dividend, divisor):
    """Determines whether dividend is divisible by divisor.

    Args:
        dividend (int): the dividend
        divisor: (non-zero int): the divisor
    Returns:
        True if divisor is divisible by divisor.
        False otherwise.
    """
    if divisor == 0:
        raise ZeroDivisionError("integer division or modulo by zero")

    n = abs(dividend) # So as to work with negative parameters
    m = abs(divisor)  # (although not necessary for this task).

    # If repeatedly subtracting the divisor from the dividend reaches zero
    # the dividend is divisible by the divisor. If this subtraction 
    # overshoots zero, the dividend is not divisible by the divisor.
    while n > 0:
        n -= m
    return n == 0


def kitkat():
    """Yields strings representing the integers from 1 to 100 in decimal.
    However, for multiples of 3 yields 'Kit' instead of the number and for
    the multiples of five yields 'Kat'. For numbers which are a multiple of
    both 3 and 5, yields 'KitKat'.

    This version does not use the modulo operator or the division operators.
    """
    # Exactly the same as in problemA.py, but substituting the divisible
    # function for the test of divisibility using the % operator.
    for n in range(1, 101):
        kit = 'Kit' if divisible(n, 3) else ''
        kat = 'Kat' if divisible(n, 5) else ''

        yield kit + kat or str(n)

if __name__ == '__main__':
    for st in kitkat():
        print(st)
