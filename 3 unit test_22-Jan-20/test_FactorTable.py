import unittest
from FactorTable import factors

class TestFactors(unittest.TestCase):
    def test_zero(self):
        self.assertRaises(ValueError,factors,0)
    def test_one(self):
        self.assertListEqual(factors(1),[1])

if __name__=="__main__":
    unittest.main()
