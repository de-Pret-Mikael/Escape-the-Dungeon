from libs.item import *
import unittest


class TestItem(unittest.TestCase):

    def test_init(self):
        items = Item(1, 1, "name", "photo")
        self.assertIsInstance(items.x, int)
        self.assertIsInstance(items.y, int)
        self.assertIsInstance(items.itemName, str)
        self.assertIsInstance(items.pType, str)
        items = Item(-1, -1, "name", "photo")
        self.assertIsInstance(items.x, int)
        self.assertIsInstance(items.y, int)
        items = Item(0, 0, "name", "photo")
        self.assertIsInstance(items.x, int)
        self.assertIsInstance(items.y, int)


if __name__ == '__main__':
    TestItem()
