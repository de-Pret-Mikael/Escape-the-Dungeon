# ▲▶▼◀■□●
import random  # import de la librairie random
from libs.chest import *


class Cell:  # creation de la clss Cell qui sera utiliser par la class Labyrinthe
    """class qui genere les cellule que labyrinthe utilisera"""
    count = 0  # donnera le numero de la cellule pour la creation du futur chemin du lanyrinthe

    def __init__(self, x, y, wall=False):
        self.__id = "{},{}".format(x, y)  # id de la cellule
        self.__x = x  # position x de la cellule
        self.__y = y  # position y de la cellule
        self.wall = wall  # si la cellule est un mur (True  ou Flase)
        self.hero = False  # la cellule possede t elle le hero (True ou False)
        self.end = False  # la cellule est la fin du Labyrinthe (True ou False)
        if not self.wall:  # seraa utiliser pour l'agorithme de generation de Labyrinthe
            self.numb = self.__class__.count
            self.__class__.count += 1
        else:
            self.numb = -1

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def id(self):
        return self.__id

    def cell_adj(self, xMax, yMax):
        """
        Fonction qui renvoie un dictionnnaire composée des position des cellule adjacente a la posiotn donnée en
        paramètre

        :param xMax: valeur max de x
        :param yMax: valeur max de y
        :return envoie un dictionnaire de dictionnnaire composé des cellule adjacente
        """
        dic = {}
        xMax = 2 * xMax
        yMax = 2 * yMax
        if self.y - 1 >= 0:
            dic["top"] = {"x": self.x, "y": self.y - 1}
        if self.x + 1 <= xMax:
            dic["right"] = {"x": self.x + 1, "y": self.y}
        if self.y + 1 <= yMax:
            dic["down"] = {"x": self.x, "y": self.y + 1}
        if self.x - 1 >= 0:
            dic["left"] = {"x": self.x - 1, "y": self.y}
        return dic


class Labyrinthe:  # creation du Labyrinthe
    """class qui genere tout le labyrinthe de façon aléatoire"""

    def __init__(self, height=3, width=3):
        self.__height = round(height)  # hauteur du Labyrinthe
        self.__width = round(width)  # largeur du Labyrinthe
        self.start = {"x": None, "y": None}  # position du debut
        self.end = {"x": None, "y": None}  # position de la fin
        self.laby = []  # tableau qui sera compose de tout les cellule du Labyrinthe
        self.wall = []  # tableau qui sera compose de tout les murs du Labyrinthe
        self.item = []
        self.build_grid()  # creation de tout les cellule
        self.build_way()  # creation du chemin graace a l'algorithme
        self.start_and_end()  # positionnement du debut e de la fin

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def get_cell(self, x, y):
        return self.laby[y][x]

    def build_grid(self):
        """
        fonction qui cree toute les cellule du Labyrinthe
        """
        self.laby = []
        line = self.height  # hauteur du Labyrinthe
        rows = self.width  # largeur du Labyrinthe
        for y in range(0, 2 * line + 1):
            self.laby.append([])
            for x in range(0, 2 * rows + 1):
                if x % 2 == 0 or y % 2 == 0:  #
                    self.laby[y].append(Cell(x, y, True))
                    if (x != 0) and (y != 0) and (x != rows * 2) and (
                            y != line * 2):  # vrai que si les cellule sont des mur interieur (pas les mur qui sont le  contour du Labyrinthe)
                        if not (x % 2 == 0 and y % 2 == 0):
                            self.wall.append(
                                self.laby[y][-1].id)  # ajoute de id de ceullue qui sont des mur dans la variable wall
                else:
                    self.laby[y].append(Cell(x, y))  # ajout de la cellule dans le varible laby

    def build_way(self):
        """fonction qui, via l'algorithme de creation de chemin, vas cree le chemin aleatoirement"""
        while self.val_verif():
            if len(self.wall):
                rand = random.randrange(0, len(self.wall))
            else:
                break
            coord = list(map(lambda y: int(y), self.wall[rand].split(",")))
            del self.wall[rand]
            cell = self.get_cell(coord[0], coord[1])
            dic = cell.cell_adj(self.width, self.height)
            if not coord[0] % 2:
                vRigth = self.get_cell(**dic["right"]).numb
                vLeft = self.get_cell(**dic["left"]).numb
                if not (vRigth == vLeft):
                    cell.wall = False
                    if (vRigth > vLeft):
                        self.new_val(vRigth, vLeft)
                    else:
                        self.new_val(vLeft, vRigth)
            if not coord[1] % 2:
                vDown = self.get_cell(**dic["down"]).numb
                vTop = self.get_cell(**dic["top"]).numb
                if not (vDown == vTop):
                    cell.wall = False
                    if (vDown > vTop):
                        self.new_val(vDown, vTop)
                    else:
                        self.new_val(vTop, vDown)

    def new_val(self, val, nVal):
        """
        fonction utiliser par buildWay qui permet de changer la valeur de certaine cellule lors de l execution
         de la fonction

        :param val: ancienne valeur de la cellule
        :param nVal: nouvelle valeur de la cellule
        """
        for y in self.laby:
            for x in y:
                if x.numb == val:
                    x.numb = nVal

    def val_verif(self):
        """fonction qui verifie si la valeur de 2 cellule sont les meme"""
        for y in self.laby:
            for x in y:
                if x.numb != 0 or x.numb != -1:
                    return True
        return False

    def hero_move(self, lastx, lasty, newx, newy):
        """
        fonction qui vas permettre de changer la position du hero en changeant la valeur hero dans les cellules

        :param lastx: ancienne position x du hero
        :param lasty: ancienne position y du hero
        :param newx: nouvelle postion x du hero
        :param newy: nouvelle postion y du hero
        """
        self.get_cell(lastx, lasty).hero = False
        self.get_cell(newx, newy).hero = True

    def pop_hero(self):
        """fonction qui ajoute le hero dans le labyrinthe a la position voulu"""
        self.get_cell(**self.start).hero = True

    def start_and_end(self):
        """fonction qui vas generer le debut et la fin du labyrinthe aleatoirement"""
        listOfCell = []
        for y in self.laby:
            for x in y:
                if not x.wall:
                    listOfCell.append(x)
        # genere un nombre aleatoire entre 0 et la longeur max du tableau listOfCell
        rand = random.randrange(0, len(listOfCell))
        celluleRandom = listOfCell[rand]  # selectionne l objet dans le tableau
        self.set_start(celluleRandom.x, celluleRandom.y)  # attribut les valeur x et y a start
        del celluleRandom  # retire la cellule du tableau pour ne pas la reutiliser
        # genere un nombre aleatoire entre 0 et la longeur max du tableau listOfCell
        rand = random.randrange(0, len(listOfCell))
        celluleRandom = listOfCell[rand]  # selectionne l objet dans le tableau
        celluleRandom.end = True
        self.set_end(celluleRandom.x, celluleRandom.y)  # attribut les valeur x et y a end
        self.pop_hero()  # appel la fonction pop_hero()

    def set_start(self, x, y):
        """
        cree le dictionnaire qui sera introduit dans la variable start

        :param x: position x du début du labyrinthe
        :param y: position y du début du labyrinthe
        """
        self.start = {"x": x, "y": y}

    def set_end(self, x, y):
        """
        cree le dictionnaire qui sera introduit dans la variable end

        :param x: position x de la fin du labyrinthe
        :param y: position y de la fin du labyrinthe
        """
        self.end = {"x": x, "y": y}

    def add_item(self, listOfItem):
        listOfCell = []
        for y in self.laby:
            for x in y:
                if not x.wall and not x.end and not x.hero:
                    listOfCell.append(x)
        for i in listOfItem:
            rand = random.randrange(0, len(listOfCell))
            cellRand = listOfCell[rand]
            self.item.append(Chest(cellRand.x, cellRand.y, i[0], i[1]))
            del cellRand

    def show(self):
        """permet de montrer le labyrinthe en console"""
        for j in self.laby:
            t = []
            for i in j:
                if i.wall:
                    t.append("■")
                elif i.hero:
                    t.append("●")
                elif i.end:
                    t.append("▼")
                else:
                    t.append("□")
            print("".join(t))

    def wall_around(self, x, y):
        """
        fonction qui return les positions des differents mur qu'il y a autour de la cellules

        :param x: position x de la cellule
        :param y: position y de la cellule
        :return: retourne une liste de l emplacement d'un mur par apport a une cellule
        """
        list = []
        dic = self.get_cell(x, y).cell_adj(self.width, self.height)
        for i in dic:
            if self.get_cell(**dic[i]).wall:
                list.append(i)
        return list

    def heroMove(self, lastx, lasty, newx, newy):
        """
        fonction qui vas changer le hero de cellule

        :param lastx: ancienne position x du hero
        :param lasty: ancienne position y du hero
        :param newx: nouvelle position x du hero
        :param newy: nouvelle position y du hero
        """
        self.get_cell(lastx, lasty).hero = False
        self.get_cell(newx, newy).hero = True


if __name__ == "__main__":
    l = Labyrinthe(3, 6)
    l.show()
