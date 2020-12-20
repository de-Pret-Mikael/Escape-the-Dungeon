from libs.hero import *
import unittest

class TestHero(unittest.TestCase):
    def test_init(self):
        self.assertEqual(self.x, 0)