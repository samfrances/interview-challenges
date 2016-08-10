#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from problemA import kitkat as kitkatA
from problemB import kitkat as kitkatB
from problemB import divisible

threes = [x * 3 for x in range(1, 35)]
fives = [x * 5 for x in range(1, 21)]

kitkat_test_sequence = ['KitKat' if x in threes and x in fives
                        else 'Kit' if x in threes
                        else 'Kat' if x in fives
                        else str(x) for x in range(1, 101)]


class TestKitKats(unittest.TestCase):

    def test_same(self):
        """Sanity check: Test that both versions of kitkat return the same
        result.
        """
        self.assertEqual(list(kitkatA()), list(kitkatB()))

    def test_correct(self):
        """Test that both versions of kitkat return the correct result."""
        for label, kitkat in ('A', kitkatA), ('B', kitkatB):
            with self.subTest(version=label):
                self.assertEqual(list(kitkat()), kitkat_test_sequence)


class TestDivisible(unittest.TestCase):

    def test_divisible(self):
        """Test that the divisible function returns the same answer as
        checking for divisibility using the modulo operator.
        """
        for i in range(-100, 101):
            for j in range(-100, 101):
                if j != 0: # Skip zero divisor
                    with self.subTest(i=i, j=j, mod=(i % j)):
                        self.assertEqual(divisible(i, j), i % j == 0)

    def test_zero_divisor(self):
        """Test that a divisor of zero raises a ZeroDivisionError."""
        self.assertRaises(ZeroDivisionError, divisible, dividend=5, divisor=0)


if __name__ == '__main__':
    unittest.main()
