import unittest
from katas.PrimeFactors import PrimeFactors

def newList(*args):
    return [arg for arg in args]

class TestPrimeFactors(unittest.TestCase):

    def testZero(self):
        self.assertRaises(ValueError, PrimeFactors.generate, 0)

    def testNegativeValue(self):
        self.assertRaises(ValueError, PrimeFactors.generate, -1)

    def testFromOneToNine(self):
        from_one_to_nine = [
            (1, []),
            (2, [2]),
            (3, [3]),
            (4, [2, 2]),
            (5, [5]),
            (6, [2, 3]),
            (7, [7]),
            (8, [2, 2, 2]),
            (9, [3, 3])
        ]
        for num, primes in from_one_to_nine:
            self.assertEqual(
                newList(*primes), PrimeFactors.generate(num),
                msg=f'Failed on {num}')


if __name__ == '__main__':
    unittest.main()