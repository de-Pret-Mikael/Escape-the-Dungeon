from .item import *
import unittest


class TestItem(unittest.TestCase):

    def test_init(self):
        item = Item(1, 2, "name", "photo")
        self.assertisinstance(item.x, int)


if __name__ == '__main__':
    TestItem()
