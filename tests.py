import unittest
from problemA import kitkat as kitkatA
from problemB import kitkat as kitkatB

threes = [x * 3 for x in range(1, 35)]
fives = [x * 5 for x in range(1, 21)]

class TestKitKats(unittest.TestCase):

	def test_same(self):
		"""Test that both versions of kitkat return the same result"""
		self.assertEqual(list(kitkatA()), list(kitkatB()))

	def test_correct(self):
		for kitkat in (kitkatA(), kitkatB()):
			for i, el in enumerate(kitkat):
				if i+1 in threes and i+1 in fives:
					self.assertEqual(el, 'KitKat')
				elif i+1 in threes:
					self.assertEqual(el, 'Kit')
				elif i+1 in fives:
					self.assertEqual(el, 'Kat')
				else:
					self.assertEqual(el, i+1)

if __name__ == '__main__':
	unittest.main()
