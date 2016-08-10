import unittest
from problemA import kitkat as kitkatA
from problemB import kitkat as kitkatB

label = {
	kitkatA: 'A',
	kitkatB: 'B'
}

threes = [x * 3 for x in range(1, 35)]
fives = [x * 5 for x in range(1, 21)]

print(threes)
print(fives)

kitkat_test_sequence = ['KitKat' if x in threes and x in fives
						else 'Kit' if x in threes
						else 'Kat' if x in fives
						else x for x in range(1, 101)]

class TestKitKats(unittest.TestCase):

	def test_same(self):
		"""Sanity check: Test that both versions of kitkat return the same result"""
		self.assertEqual(list(kitkatA()), list(kitkatB()))

	def test_correct(self):
		"""Test that both versions of kitkat return the correct result"""
		for label, kitkat in ('A', kitkatA), ('B', kitkatB):
			with self.subTest(version=label):
				self.assertEqual(list(kitkat()), kitkat_test_sequence)

if __name__ == '__main__':
	unittest.main()
