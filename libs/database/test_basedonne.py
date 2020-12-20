from basedonne import *
import unittest

class TestBasedonne(unittest.TestCase):
    def test_init(self):
        db = Data("str")
        self.assertIsInstance(db.path,str)

    def test_is_db_exist(self):
        db = Data("str")
        db2 = Data("../../DATA/escape-the-donjon.db")
        self.assertFalse(db.is_db_exist())
        self.assertTrue(db2.is_db_exist())

    def test_connect(self):
        db = Data("str")
        with self.assertRaises(sqlite3.Error):
            db.connect()


if __name__ == '__main__':
    TestBasedonne()