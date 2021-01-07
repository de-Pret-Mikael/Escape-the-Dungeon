from libs.hero import *
import unittest


class TestEntite(unittest.TestCase):
    def test_init(self):
        entite = Entite()
        self.assertIsInstance(entite.x, int)
        self.assertIsInstance(entite.y, int)
        self.assertIsInstance(entite.lastx, int)
        self.assertIsInstance(entite.lasty, int)
        entite = Entite()
        self.assertIsInstance(entite.x, int)
        self.assertIsInstance(entite.y, int)
        self.assertIsInstance(entite.lastx, int)
        self.assertIsInstance(entite.lasty, int)
        entite = Entite()
        self.assertIsInstance(entite.x, int)
        self.assertIsInstance(entite.y, int)
        self.assertIsInstance(entite.lastx, int)
        self.assertIsInstance(entite.lasty, int)

    def test_setPosi(self):
        posi = Entite()
        posi.set_posi(1, 1)
        self.assertEqual(posi.x, 1)
        self.assertEqual(posi.y, 1)
        posi.set_posi(-1, -1)
        self.assertEqual(posi.x, -1)
        self.assertEqual(posi.y, -1)
        posi.set_posi(0, 0)
        self.assertEqual(posi.x, 0)
        self.assertEqual(posi.y, 0)

    def test_passe(self):
        passe = Entite()
        passe.passe(1, 1)
        self.assertEqual(passe.x, 0)
        self.assertEqual(passe.y, 0)
        passe.passe(-1, -1)
        self.assertEqual(passe.x, 0)
        self.assertEqual(passe.y, 0)
        passe.passe(0, 0)
        self.assertEqual(passe.x, 0)
        self.assertEqual(passe.y, 0)

    def test_droite(self):
        droite = Entite()
        droite.x = 1
        droite.droite()
        self.assertEqual(droite.x, 2)
        droite.x = -1
        droite.droite()
        self.assertEqual(droite.x, 0)
        droite.x = 0
        droite.droite()
        self.assertEqual(droite.x, 1)

    def test_gauche(self):
        gauche = Entite()
        gauche.x = 1
        gauche.gauche()
        self.assertEqual(gauche.x, 0)
        gauche.x = -1
        gauche.gauche()
        self.assertEqual(gauche.x, -2)
        gauche.x = 0
        gauche.gauche()
        self.assertEqual(gauche.x, -1)

    def test_haut(self):
        haut = Entite()
        haut.y = 1
        haut.haut()
        self.assertEqual(haut.y, 0)
        haut.y = -1
        haut.haut()
        self.assertEqual(haut.y, -2)
        haut.y = 0
        haut.haut()
        self.assertEqual(haut.y, -1)

    def test_bas(self):
        bas = Entite()
        bas.y = 1
        bas.bas()
        self.assertEqual(bas.y, 2)
        bas.y = -1
        bas.bas()
        self.assertEqual(bas.y, 0)
        bas.y = 0
        bas.bas()
        self.assertEqual(bas.y, 1)


class TestHero(unittest.TestCase):

    def test_init(self):
        heros = Hero()
        self.assertIsInstance(heros.decal, int)
        self.assertIsInstance(heros.vie, int)
        self.assertIsInstance(heros.maxVie, int)
        self.assertIsInstance(heros.nbrTouche, int)
        self.assertIsInstance(heros.fin, bool)
        self.assertIsInstance(heros.soldier, bool)
        self.assertIsInstance(heros.touche, bool)
        self.assertIsInstance(heros.inventair, list)
        heros.score = None
        self.assertIsNone(heros.score)

    def test_move_droite(self):
        droite = Hero()
        droite.x = 1
        droite.droite()
        self.assertEqual(droite.x, 2)

    def test_end(self):
        end = Hero()
        end.end(1, 1)
        self.assertEqual(end.x, 0)
        self.assertEqual(end.y, 0)
        end = Hero()
        end.end(-1, -1)
        self.assertEqual(end.x, 0)
        self.assertEqual(end.y, 0)
        end = Hero()
        end.end(0, 0)
        self.assertEqual(end.x, 0)
        self.assertEqual(end.y, 0)

    def test_inventaire(self):
        add_inventaire = Hero()
        add_inventaire.score = 100
        add_inventaire.add_inventaire("cleBronze")
        self.assertIsInstance(add_inventaire, object)
        self.assertEqual(add_inventaire.score, 300)

    def test_is_touche(self):
        is_touche = Hero()
        is_touche.mobs = None
        self.assertIsNone(is_touche.mobs)
        if is_touche.touche:
            is_touche.nbrTouche = 40
            is_touche.is_touche()
            self.assertEqual(is_touche.nbrTouche, 39)
            if is_touche.nbrTouche == 0:
                self.assertEqual(is_touche.touche, False)
        self.assertEqual(is_touche.nbrTouche, 40)

    def test_set_score(self):
        set_score = Hero()
        set_score.set_score(100)
        self.assertEqual(set_score.score, 100)


class TestMonstre(unittest.TestCase):
    def test_init(self):
        monstre = Monstre()
        self.assertIsInstance(monstre.color, str)
        self.assertIsInstance(monstre.typeMonstre, str)
        monstre.puissance = None
        self.assertIsNone(monstre.puissance)

    def test_str(self):
        self.assertEqual(str(1), "1")
        self.assertEqual(str(-1), "-1")
        self.assertEqual(str(0), "0")


if __name__ == '__main__':
    TestEntite()
    TestHero()
    TestMonstre()
