from random import *

from libs.labyrinthe import labyrinthe


class Hero:

    def __init__(self):
        self.__x = 0  # position x du héro
        self.__y = 0  # position y du héro
        self.__decal = 0  # déplacement du héro
        self.lastx = 0  # avant dernière position x du héro
        self.lasty = 0  # avant dernière position y du héro
        self.fin = False  # le jeu est t'il fini (True/False)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def decal(self):
        return self.__decal

    @x.setter
    def x(self, i):
        if not isinstance(i, int):
            raise ValueError("not integer")
        self.__x = i

    @y.setter
    def y(self, i):
        if not isinstance(i, int):
            raise ValueError("not integer")
        self.__y = i

    @decal.setter
    def decal(self, i):
        if not isinstance(i, int):
            raise ValueError("not integer")
        self.__decal = i

    def setPosi(self, x, y):
        """Position du héro au départ"""
        self.x = x
        self.y = y

    def droite(self, laby):
        """Fonction pour ce déplacer d' un pas saut s'il y a un mur"""
        self.passe(self.x, self.y)
        if laby.get_cell(self.x + 1, self.y).wall:
            print('Vous ne pouvez pas traverser les murs :(')
        else:
            self.x += 1

    def gauche(self, laby):
        """Fonction pour ce déplacer d' un pas saut s'il y a un mur"""
        self.passe(self.x, self.y)
        if laby.get_cell(self.x - 1, self.y).wall:
            print('Vous ne pouvez pas traverser les murs :(')
        else:
            self.x -= 1

    def haut(self, laby):
        """Fonction pour ce déplacer d' un pas saut s'il y a un mur"""
        self.passe(self.x, self.y)
        if laby.get_cell(self.x, self.y - 1).wall:
            print('Vous ne pouvez pas traverser les murs :(')
        else:
            self.y -= 1

    def bas(self, laby):
        """Fonction pour ce déplacer d' un pas saut s'il y a un mur"""
        self.passe(self.x, self.y)
        if laby.get_cell(self.x, self.y + 1).wall:
            print('Vous ne pouvez pas traverser les murs :(')
        else:
            self.y += 1

    def choix_deplacement(self, laby):
        """Fonction demandant qu'elle déplacement veut faire le joueur"""
        decal = 0
        condi = True
        while condi:
            decal = input(
                "appuyez sur 6 pour droite, 4 pour gauche, 2 pour bas et 8 pour haut et 5 pour exit puis ENTER ")
            if decal == '6' or decal == '4' or decal == '2' or decal == '8' or decal == '5':
                condi = False
            else:
                print('Mauvais caractère')

        if decal == '6':
            self.droite(laby)
        if decal == '8':
            self.haut(laby)
        if decal == '4':
            self.gauche(laby)
        if decal == '2':
            self.bas(laby)
        if decal == '5':
            self.end(**laby.end)

    def passe(self, lastx, lasty):
        """avant dernière position du héro"""
        self.lastx = lastx
        self.lasty = lasty

    def end(self, x, y):
        """permet au joueur de quitter"""
        if x == self.x and y == self.y:
            fini = input('êtes vous sur y/n: ')
            if fini == 'y':
                self.fin = True

    def move(self, char, laby):
        if char == "d":
            self.droite(laby)
        if char == "z":
            self.haut(laby)
        if char == "q":
            self.gauche(laby)
        if char == "s":
            self.bas(laby)


if __name__ == "__main__":
    l = Labyrinthe(3, 6)
    pnj = hero()
    print(pnj)
    pnj.x = randint(1, 8)
    pnj.y = randint(1, 8)
    print(pnj.x, pnj.y, pnj.lastx, pnj.lasty)
    pnj.choix_deplacement(l)
    print(pnj.x, pnj.y, pnj.lastx, pnj.lasty)
