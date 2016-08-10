#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""problemA.py: Prints the numbers from 1 to 100, one per line.  However for
multiples of 3 prints “Kit” instead of the number and for the multiples of
five print “Kat”.  For numbers which are a multiple of both 3 and 5, prints
“KitKat”.
"""


def kitkat():
    """Yields strings representing the integers from 1 to 100 in decimal.
    However, for multiples of 3 yields 'Kit' instead of the number and for
    the multiples of five yields 'Kat'. For numbers which are a multiple of
    both 3 and 5, yields 'KitKat'.

    This version uses the modulo operator to test for divisibility.
    """

    for n in range(1, 101):
        kit = 'Kit' if n % 3 == 0 else ''
        kat = 'Kat' if n % 5 == 0 else ''

        # Taking advantage of the truthy-ness of non-empty strings, and the
        # falsy-ness of empty strings, kit / kat act both as flags
        # indicating divisibility by 3 / 5, and as the strings to return
        # in case of such divisibility.

        yield kit + kat or str(n)  # Short-circuiting

if __name__ == '__main__':
    for st in kitkat():
        print(st)
