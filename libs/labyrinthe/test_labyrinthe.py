from libs.labyrinthe import *
import unittest


class TestLabyrinthe(unittest.TestCase):
    def test_init(self):
        laby = Labyrinthe(3, 3)
        self.assertEqual(laby.height, 3)
        self.assertEqual(laby.width, 3)
        self.assertIsInstance(laby.laby, list)
        self.assertIsInstance(laby.wall, list)
        self.assertIsInstance(laby.mobs, list)
        self.assertIsInstance(laby.item, list)
        self.assertIsInstance(laby.start, dict)
        self.assertIsInstance(laby.end, dict)

    def test_get_cell(self):
        laby = Labyrinthe(3, 3)
        self.assertEqual(laby.get_cell(1, 1).x, 1)
        self.assertEqual(laby.get_cell(1, 2).y, 2)

    def test_hero_move(self):
        laby = Labyrinthe(3, 3)
        newx, newy, lastx, lasty = 1, 1, 1, 2
        new = {"x": newx, "y": newy}
        last = {"x": lastx, "y": lasty}
        coord = {"newx": newx, "newy": newy, "lastx": lastx, "lasty": lasty}
        laby.hero_move(**coord)
        self.assertTrue(laby.get_cell(**new).hero)
        self.assertFalse(laby.get_cell(**last).hero)

    def test_mobs_move(self):
        laby = Labyrinthe(3, 3)
        newx, newy, lastx, lasty = 1, 1, 1, 2
        new = {"x": newx, "y": newy}
        last = {"x": lastx, "y": lasty}
        coord = {"newx": newx, "newy": newy, "lastx": lastx, "lasty": lasty}
        laby.mobs_move(**coord)
        self.assertTrue(laby.get_cell(**new).mobs)
        self.assertFalse(laby.get_cell(**last).mobs)

    def test_pop_hero(self):
        laby = Labyrinthe(3, 3)
        laby.pop_hero()
        self.assertTrue(laby.get_cell(**laby.start).hero)

    def test_pop_mobs(self):
        laby = Labyrinthe(3, 3)
        x, y = 1, 2
        laby.pop_mobs(x, y)
        self.assertTrue(laby.get_cell(x, y).mobs)

    def test_wall_around(self):
        laby = Labyrinthe(3, 3)
        self.assertIsInstance(laby.wall_around(1, 1), list)
