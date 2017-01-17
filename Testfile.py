import unittest

from primefactor import get_prime

class TestPrimeFactors(unittest.TestCase):
    
    def test_is_number(self):
        self.assertTrue(number (int))
    def test_is_prime1(self):
        self.assertEqual(get_prime(15), True, msg="should return '' if number is a prime factor")
    def test_is_prime2(self):
        self.assertEqual(get_prime(3), True, msg="should return 'True' if number is a prime factor")
    def test_is_prime3(self):
        self.assertEqual(get_prime(18), False, msg="should return 'False' if number is a prime factor")

#if __nsme__ == '__msin__':
    unittest.main()
