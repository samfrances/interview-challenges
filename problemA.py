#!/usr/bin/env python3

# Version 1 of kitkat, where use of the % operator is permitted

def kitkat():
    """Yields strings representing the integers from 1 to 100 in decimal. 
    However for multiples of 3
    yields 'Kit' instead of the number and for the multiples of five yields
    'Kat'.  For numbers which are a multiple of both 3 and 5, yields 'KitKat'.

    This version uses the modulo operator to test for divisibility."""

    for n in range(1, 101):
        kit = 'Kit' if n % 3 == 0 else ''
        kat = 'Kat' if n % 5 == 0 else ''
        
        yield kit + kat or str(n)

if __name__ == '__main__':
    for st in kitkat():
        print(st)

