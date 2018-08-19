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

    def testPowersOfTen(self):
        def generatePrimesOfPowersOfTen(n):
            primes = [2, 5]
            for _ in range(n):
                yield primes
                primes = [2] + primes + [5]

        powers_of_ten = [(10**i, primes) for i, primes in enumerate(generatePrimesOfPowersOfTen(8), start=1)]
        for num, primes in powers_of_ten:
            self.assertEqual(
                newList(*primes), PrimeFactors.generate(num),
                msg=f'Failed on {num}')

    def testTenPickedNumbers(self):
        ten_picked_numbers = [
            (101, [101]),
            (231, [3, 7, 11]),
            (403, [13, 31]),
            (490, [2, 5, 7, 7]),
            (588, [2, 2, 3, 7, 7]),
            (654, [2, 3, 109]),
            (711, [3, 3, 79]),
            (883, [883]),
            (960, [2, 2, 2, 2, 2, 2, 3, 5]),
            (999, [3, 3, 3, 37])
        ]
        for num, primes in ten_picked_numbers:
            self.assertEqual(
                newList(*primes), PrimeFactors.generate(num),
                msg=f'Failed on {num}')

if __name__ == '__main__':
    unittest.main()