import basic
import unittest

class TestCalc(unittest.TestCase):
    

    def test_add(self):
        """ testing add function"""
        self.assertEqual(basic.add(4, 3), 7, "Error should be 7")
        self.assertEqual(basic.add(4, 3, 2), 9, "error should be 9")
        return None

    def test_mul(self):
        """ testing mul function"""
        self.assertEqual(basic.mul(4, 3), 13, "Error should be 13")
        self.assertEqual(basic.mul(4, 3, 2), 24, "error should be 24")
        return None


    def test_div(self):
        self.assertEqual(basic.div(4, 3), 1.334, "Error should be 1.334")



if __name__ == "__main__":
    unittest.main()