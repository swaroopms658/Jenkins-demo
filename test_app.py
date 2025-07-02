# test_app.py

import unittest
from app import reverse_string

class TestApp(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("12345"), "54321")
        self.assertNotEqual(reverse_string("abc"), "abc")  # to ensure it's not unchanged

if __name__ == '__main__':
    unittest.main()
