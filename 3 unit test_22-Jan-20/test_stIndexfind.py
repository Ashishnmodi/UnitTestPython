import unittest
from stindexfind import StrIndexFinder

class TestStIndex(unittest.TestCase):
    def test_st(self):
        self.assertRaises(AttributeError, StrIndexFinder, None, None)
        self.assertRaises(AttributeError, StrIndexFinder, 'Hello', None)
        self.assertRaises(AttributeError, StrIndexFinder, None,'Hello')
    def test_stout(self):
        self.assertAlmostEqual(StrIndexFinder("Hello","ll"),2)
if __name__ == '__main__':
    unittest.main()
