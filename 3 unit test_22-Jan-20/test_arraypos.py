import unittest
from arraypos import arr_pos

class TestArray(unittest.TestCase):
    def test_val(self):
        self.assertRaises(ValueError,arr_pos,0,-1,2,3,4)

    def test_type(self):
        self.assertRaises(TypeError,arr_pos,2,{2,3,5,7,8})

if __name__ == '__main__':
    unittest.main()
