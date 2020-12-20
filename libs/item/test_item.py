from item import *
import unittest


class TestItem(unittest.TestCase):

    def test_init(self):
        item = Item(1, 2, "name", "photo")
        self.assertIsInstance(item.x, int)
        self.assertIsInstance(item.y, int)


if __name__ == '__main__':
    TestItem()
