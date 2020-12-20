import random


class Entite:
    """
    PRE : -
    POST : donne la valeur 0 à x, y, lastx et lasty
    """
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
        """
        PRE : x et y doivent être de type integer
        POST : donne la position x et y au variable x et y
        """
        self.x = x
        self.y = y

    def passe(self, lastx, lasty):
        """avant dernière position du héro"""
        """
        PRE : lastx et lasty doivent être de type integer
        POST : donne les dernière position x et y
        """
        self.lastx = lastx
        self.lasty = lasty

    def droite(self):
        """
        POST : rajoute 1 à x
        """
        self.x += 1

    def gauche(self):
        """
        POST : enlève 1 à x
        """
        self.x -= 1

    def haut(self):
        """
        POST : enlève 1 à y
        """
        self.y -= 1

    def bas(self):
        """
        POST : rajoute 1 à y
        """
        self.y += 1


class Hero(Entite):
    def __init__(self):
        """
        POST : donne la valeur 0 à décal, False à fin et touche, True à soldier, gold à color, une liste vide à inventaire, None à score, 3 à vie et maxVie et 40 à nbrTouche
        """
        super().__init__()
        self.__decal = 0
        self.fin = False
        self.soldier = True
        self.color = "gold"
        self.inventair = []
        self.vie = 3
        self.maxVie = 3
        self.score = None
        self.touche = False
        self.nbrTouche = 40

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
        """
        PRE : Le déplacement ne doit pas être vers un mur et laby est l'objet labyrinthe
        POST : Permet un déplacement vers la droite et d'entré en combat avec un mobs
        """
        self.passe(self.x, self.y)
        cellule = laby.get_cell(self.x + 1, self.y)
        if cellule.wall:
            print('Vous ne pouvez pas traverser les murs :(')
        elif cellule.mobs:
            self.combat(laby, self.x + 1, self.y)
            print('Engage le combat :)')
        elif not self.is_mobs_around(laby):
            self.droite()

    def move_gauche(self, laby):
        """Fonction pour ce déplacer d' un pas saut s'il y a un mur"""
        """
        PRE : Le déplacement ne doit pas être vers un mur et laby est l'objet labyrinthe
        POST : Permet un déplacement vers la gauche et d'entré en combat avec un mobs
        """
        self.passe(self.x, self.y)
        cellule = laby.get_cell(self.x - 1, self.y)
        if cellule.wall:
            print('Vous ne pouvez pas traverser les murs :(')
        elif cellule.mobs:
            self.combat(laby, self.x - 1, self.y)
            print('Engage le combat :)')
        elif not self.is_mobs_around(laby):
            self.gauche()

    def move_haut(self, laby):
        """Fonction pour ce déplacer d' un pas saut s'il y a un mur"""
        """
        PRE : Le déplacement ne doit pas être vers un mur et laby est l'objet labyrinthe
        POST : Permet un déplacement vers la haut et d'entré en combat avec un mobs
        """
        self.passe(self.x, self.y)
        cellule = laby.get_cell(self.x, self.y - 1)
        if cellule.wall:
            print('Vous ne pouvez pas traverser les murs :(')
        elif cellule.mobs:
            self.combat(laby, self.x, self.y - 1)
            print('Engage le combat :)')
        elif not self.is_mobs_around(laby):
            self.haut()

    def move_bas(self, laby):
        """Fonction pour ce déplacer d' un pas saut s'il y a un mur"""
        """
        PRE : Le déplacement ne doit pas être vers un mur et laby est l'objet labyrinthe
        POST : Permet un déplacement vers la bas et d'entré en combat avec un mobs
        """
        self.passe(self.x, self.y)
        cellule = laby.get_cell(self.x, self.y + 1)
        if cellule.wall:
            print('Vous ne pouvez pas traverser les murs :(')
        elif cellule.mobs:
            self.combat(laby, self.x, self.y + 1)
            print('Engage le combat :)')
        elif not self.is_mobs_around(laby):
            self.bas()

    def choix_deplacement(self, laby):
        """Fonction demandant qu'elle déplacement veut faire le joueur"""
        """
        PRE : condi doit valoir True et laby est l'objet labyrinthe
        POST : donne 0 à decal et True à condi et appel les fonctions permetant de ce déplacer ou de quitter 
        """
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
        """
        PRE : La position du joueur doit être égal à celle de la fin et x et y doivent être des integer
        POST : passe fin à True pour quitter
        """
        if x == self.x and y == self.y:
            fini = input('êtes vous sur y/n: ')
            if fini == 'y':
                self.fin = True


    def add_inventaire(self, item):
        """
        PRE : item doit être un objet photo
        POST : rajoute les item à la liste inventaire et permet d'augmenter le score
        """
        self.inventair.append(item)
        self.score += 200

    def combat(self, laby, mobsx, mobsy):
        """
        PRE : laby est l'object labirynthe, mobsx et mobsy doivent des integer
        POST : Permet de combrattre un monstre, le faire mourir(disparaitre) et augmenter le score
        """
        number = random.randint(1, 6)
        print(number)
        id = "{},{}".format(mobsx, mobsy)
        mobs = None
        for i in laby.mobs:
            if id == i.id:
                mobs = i
        if mobs.puissance > number:
            self.vie -= 1
            laby.get_cell(mobsx, mobsy).mobs = False
            laby.del_mobs(mobsx, mobsy)
            self.touche = True
        else:
            self.score += 100 * mobs.puissance
            laby.get_cell(mobsx, mobsy).mobs = False
            laby.del_mobs(mobsx, mobsy)


    def is_touche(self):
        """
        POST : Vérifie si le monstre à toucher le héro
        """
        if self.touche:
            self.nbrTouche -= 1
            if self.nbrTouche == 0:
                self.touche = False
                return False
            else:
                return True
        self.nbrTouche = 40
        return False


    def is_mobs_around(self, laby):
        """
        PRE : laby est l'objet labyrinthe
        POST : Vérifie si un mobs ce trouve à côté du héro
        """
        dictAdj = laby.get_cell(self.x, self.y).cell_adj(laby.width, laby.height)
        for i in dictAdj:
            if laby.get_cell(**dictAdj[i]).mobs:
                return True
        return False

    def set_score(self, score):
        self.score = score


class Monstre(Entite):
    def __init__(self):
        """
        POST : Donne bleu à color, ork1 à typeMonstre, None à puissance et super permet d' hérité du init de la class entité
        """
        super().__init__()
        self.color = "blue"
        self.typeMonstre = "ork1"
        self.puissance = None

    @property
    def id(self):
        return "{},{}".format(self.x, self.y)

    @property
    def pathImg(self):
        return "img/mobs/{}".format(self.color)

    def __str__(self):
        """
        POST : renvoie sous forme de string la position du héro au départ
        """
        return "x:{} y:{}".format(self.x, self.y)

    def deplacement(self, laby):
        """
        PRE : value doit être égal à top, right, down ou left et laby est l'objet labyrinthe
        POST : donne la forme string de top, right, down et left
        """
        top, right, down, left = "top", "right", "down", "left"
        dicAdj = laby.get_cell(self.x, self.y).cell_adj(laby.width, laby.height)
        liste = laby.wall_around(self.x, self.y)
        possible = []
        is_hero = False
        for i in [top, right, down, left]:
            hero = laby.get_cell(**dicAdj[i]).hero
            if hero:
                is_hero = True
            if i not in liste and not laby.exist_mobs(**dicAdj[i]) and not hero:
                possible.append(i)
        if is_hero:
            pass
        else:
            if len(possible) != 0:
                rand = random.randrange(0, len(possible))
                value = possible[rand]
                self.passe(self.x, self.y)
                if value == top:
                    self.haut()
                if value == right:
                    self.droite()
                if value == down:
                    self.bas()
                if value == left:
                    self.gauche()

            laby.mobs_move(self.lastx, self.lasty, self.x, self.y)


if __name__ == "__main__":
    pass