import unittest
from app import total
class AppTest(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total(25, 3), 75)
