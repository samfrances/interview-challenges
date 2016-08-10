#!/usr/bin/env python3

# Version 1 of kitkat, where use of the % operator is permitted

def kitkat():
    """Prints the numbers from 1 to 100, one per line.  However for multiples of 3
    print 'Kit' instead of the number and for the multiples of five print
    'Kat'.  For numbers which are a multiple of both 3 and 5, print 'KitKat'.

    This version uses the modulo operator."""

    for n in range(1, 101):
        kit = 'Kit' if n % 3 == 0 else ''
        kat = 'Kat' if n % 5 == 0 else ''
        
        if not (kit or kat):
            yield n
        else:
            yield "{0}{1}".format(kit, kat)

if __name__ == '__main__':
    for st in kitkat():
        print(st)

