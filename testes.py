import unittest
from main import Fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    
    def setUp(self):
        self.fizzbuzz = Fizzbuzz()
    
    def test_fizz(self):
        self.assertEqual(self.fizzbuzz._regras(3), "fizz")
        self.assertEqual(self.fizzbuzz._regras(6), "fizz")
    
    def test_buzz(self):
        self.assertEqual(self.fizzbuzz._regras(5), "buzz")
        self.assertEqual(self.fizzbuzz._regras(10), "buzz")
    
    def test_fizzbuzz(self):
        self.assertEqual(self.fizzbuzz._regras(15), "fizzbuzz")
        self.assertEqual(self.fizzbuzz._regras(30), "fizzbuzz")
    
    def test_numero(self):
        self.assertEqual(self.fizzbuzz._regras(1), "1")
        self.assertEqual(self.fizzbuzz._regras(2), "2")

if __name__ == '__main__':
    unittest.main()
