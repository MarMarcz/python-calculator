# test_calculator.py
import unittest
from calculator import multiply

class TestCalculator(unittest.TestCase):
    
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 3), 0)
        self.assertEqual(multiply(-2, -2), 4)
        #self.assertEqual(multiply(-2, -2), 1) # This test will fail
        
if __name__ == "__main__":
    unittest.main()
