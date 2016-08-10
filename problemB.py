#!/usr/bin/env python3

# Version 2 of kitkat, where use of the % / or // operators is not permitted

def divisible(n, by):
    """Assumes n and by are positive integers.
    Returns True if n is divisible by by, else False"""

    while n > 0:
        n -= by
    return n == 0

def kitkat():
    """Yields the numbers from 1 to 100, one per line.  However for multiples of 3
    print 'Kit' instead of the number and for the multiples of five print
    'Kat'.  For numbers which are a multiple of both 3 and 5, print 'KitKat'.

    This version does not use the modulo operator or the division operators."""

    for n in range(1, 101):
        kit = 'Kit' if divisible(n, 3) else ''
        kat = 'Kat' if divisible(n, 5) else ''
        
        if not (kit or kat):
            yield n
        else:
            yield "{0}{1}".format(kit, kat)

if __name__ == '__main__':
    for st in kitkat():
        print(st)

    

