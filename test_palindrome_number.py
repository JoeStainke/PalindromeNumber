import unittest
import palindrome_number

class TestPalindromeNumber(unittest.TestCase):

    def test_true(self):
        self.assertTrue(palindrome_number.is_num_palindrome(121))
        self.assertFalse(palindrome_number.is_num_palindrome(10))

if __name__ == '__main__':
    unittest.main()