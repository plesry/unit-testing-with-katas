import unittest
from katas.PrimeFactors import PrimeFactors

def newList(*args):
    return [arg for arg in args]

class TestPrimeFactors(unittest.TestCase):

    def testOne(self):
        self.assertEquals(newList(), PrimeFactors.generate(1))


if __name__ == '__main__':
    unittest.main()