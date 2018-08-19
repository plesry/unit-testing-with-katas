import unittest
from katas.PrimeFactors import PrimeFactors

def newList(*args):
    return [arg for arg in args]

class TestPrimeFactors(unittest.TestCase):

    def testOne(self):
        self.assertEquals(newList(), PrimeFactors.generate(1))

    def testTwo(self):
        self.assertEquals(newList(2), PrimeFactors.generate(2))

    def testThree(self):
        self.assertEquals(newList(3), PrimeFactors.generate(3))

    def testFour(self):
        self.assertEquals(newList(2, 2), PrimeFactors.generate(4))

    def testFive(self):
        self.assertEquals(newList(5), PrimeFactors.generate(5))


if __name__ == '__main__':
    unittest.main()