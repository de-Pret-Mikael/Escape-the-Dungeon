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
        posi.setPosi(1, 1)
        self.assertEqual(posi.x, 1)
        self.assertEqual(posi.y, 1)
        posi.setPosi(-1, -1)
        self.assertEqual(posi.x, -1)
        self.assertEqual(posi.y, -1)
        posi.setPosi(0, 0)
        self.assertEqual(posi.x, 0)
        self.assertEqual(posi.y, 0)


    def test_passe(self):
        passe = Entite()
        passe.setPosi(1, 1)
        self.assertEqual(passe.x, 1)
        self.assertEqual(passe.y, 1)
        passe.setPosi(-1, -1)
        self.assertEqual(passe.x, -1)
        self.assertEqual(passe.y, -1)
        passe.setPosi(0, 0)
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
        hero = Hero()
        self.assertIsInstance(hero.decal, int)
        self.assertIsInstance(hero.vie, int)
        self.assertIsInstance(hero.maxVie, int)
        self.assertIsInstance(hero.nbrTouche, int)
        self.assertIsInstance(hero.fin, bool)
        self.assertIsInstance(hero.soldier, bool)
        self.assertIsInstance(hero.touche, bool)
        self.assertIsInstance(hero.inventair, list)
        hero.score = None
        self.assertIsNone(hero.score)

    def test_move_droite(self):
        droite = Hero()
        droite.x = 1
        droite.droite()
        self.assertEqual(droite.x, 2)

    def test_choix_deplacement(self):
        deplacement = Hero()
        self.assertIsInstance(deplacement.decal, int)
        #self.assertEqual(deplacement.condi, bool)
        #deplacement.decal = '6'
        #deplacement.choix_deplacement()
        #self.assertEqual('6', )

    def end(self):
        end = Hero(1, 1)
        end.x = 1
        self.assertEqual(end.x, 1)




if __name__ == '__main__':
    TestHero()
