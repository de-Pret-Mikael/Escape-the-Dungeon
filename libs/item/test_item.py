from libs.item import *
import unittest


class TestItem(unittest.TestCase):

    def test_init(self):
        item = Item(1, 1, "name", "photo")
        self.assertIsInstance(item.x, int)
        self.assertIsInstance(item.y, int)
        self.assertIsInstance(item.itemName, str)
        self.assertIsInstance(item.pType, str)
        item = Item(-1, -1, "name", "photo")
        self.assertIsInstance(item.x, int)
        self.assertIsInstance(item.y, int)
        item = Item(0, 0, "name", "photo")
        self.assertIsInstance(item.x, int)
        self.assertIsInstance(item.y, int)

if __name__ == '__main__':
    TestItem()