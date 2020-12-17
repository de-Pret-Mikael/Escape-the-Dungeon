import random


class Entite:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.lastx = 0
        self.lasty = 0

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

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

    def setPosi(self, x, y):
        """Position du héro au départ"""
        self.x = x
        self.y = y

    def passe(self, lastx, lasty):
        """avant dernière position du héro"""
        self.lastx = lastx
        self.lasty = lasty

    def droite(self):
        self.x += 1

    def gauche(self):
        self.x -= 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1


class Hero(Entite):
    def __init__(self):
        super().__init__()
        self.__decal = 0  # déplacement du héro
        self.fin = False  # le jeu est t'il fini (True/False)
        self.soldier = True
        self.color = "red"
        self.inventair = []

    @property
    def decal(self):
        return self.__decal

    @decal.setter
    def decal(self, i):
        if not isinstance(i, int):
            raise ValueError("not integer")
        self.__decal = i

    def move_droite(self, laby):
        """Fonction pour ce déplacer d' un pas saut s'il y a un mur"""
        self.passe(self.x, self.y)
        if laby.get_cell(self.x + 1, self.y).wall:
            print('Vous ne pouvez pas traverser les murs :(')
        else:
            self.droite()

    def move_gauche(self, laby):
        """Fonction pour ce déplacer d' un pas saut s'il y a un mur"""
        self.passe(self.x, self.y)
        if laby.get_cell(self.x - 1, self.y).wall:
            print('Vous ne pouvez pas traverser les murs :(')
        else:
            self.gauche()

    def move_haut(self, laby):
        """Fonction pour ce déplacer d' un pas saut s'il y a un mur"""
        self.passe(self.x, self.y)
        if laby.get_cell(self.x, self.y - 1).wall:
            print('Vous ne pouvez pas traverser les murs :(')
        else:
            self.haut()

    def move_bas(self, laby):
        """Fonction pour ce déplacer d' un pas saut s'il y a un mur"""
        self.passe(self.x, self.y)
        if laby.get_cell(self.x, self.y + 1).wall:
            print('Vous ne pouvez pas traverser les murs :(')
        else:
            self.bas()

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
            self.move_droite(laby)
        if decal == '8':
            self.move_haut(laby)
        if decal == '4':
            self.move_gauche(laby)
        if decal == '2':
            self.move_bas(laby)
        if decal == '5':
            self.end(**laby.end)

    def end(self, x, y):
        """permet au joueur de quitter"""
        if x == self.x and y == self.y:
            fini = input('êtes vous sur y/n: ')
            if fini == 'y':
                self.fin = True

    def move(self, char, laby):
        if char == "d":
            self.move_droite(laby)
        if char == "z":
            self.move_haut(laby)
        if char == "q":
            self.move_gauche(laby)
        if char == "s":
            self.move_bas(laby)

    def add_inventaire(self, item):
        self.inventair.append(item)


class Monstre(Entite):
    def __init__(self):
        super().__init__()
        self.color = "blue"
        self.typeMonstre = "ork1"  # ork1 ork2 slime1 slime2 slime3
        self.life = None

    @property
    def id(self):
        return "{},{}".format(self.x, self.y)

    @property
    def pathImg(self):
        return "img/mobs/{}".format(self.color)

    def __str__(self):
        return "x:{} y:{}".format(self.x, self.y)

    def deplacement(self, laby):
        top, right, down, left = "top", "right", "down", "left"
        liste = laby.wall_around(self.x, self.y)
        possible = []
        for i in [top, right, down, left]:
            if i not in liste:
                possible.append(i)
        rand = random.randrange(0, len(possible))
        value = possible[rand]
        if value == top:
            self.haut()
        if value == right:
            self.droite()
        if value == down:
            self.bas()
        if value == left:
            self.gauche()


if __name__ == "__main__":
    pass