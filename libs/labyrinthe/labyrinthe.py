# ▲▶▼◀■□●
import random  # import de la librairie random
from libs.item import *
from libs.hero import Monstre


class Cell:  # creation de la class Cell qui sera utiliser par la class Labyrinthe
    """class qui génère les cellule que labyrinthe utilisera"""
    count = 0  # donnera le numéro de la cellule pour la creation du futur chemin du labyrinthe

    def __init__(self, x, y, wall=False):
        """
        PRE : x et y doivent être un Int, wall doit être un boolean

        POST : initialise l'objet cellule
            id prend comme valeur "x,y"
            x prend comme valeur le paramètre x
            y prend comme valeur le paramètre y
            wall prend comme valeur le paramètre wall
            hero prend comme valeur False
            end prend comme valeur False
            numb prend comme valeur le count si c'est pas un un mur, sinon prend comme valeur -1
        """
        self.__id = "{},{}".format(x, y)  # id de la cellule
        self.__x = x  # position x de la cellule
        self.__y = y  # position y de la cellule
        self.wall = wall  # si la cellule est un mur (True  ou False)
        self.hero = False  # la cellule possède t elle le hero (True ou False)
        self.end = False  # la cellule est la fin du Labyrinthe (True ou False)
        if not self.wall:  # sera utiliser pour l'algorithme de generation de Labyrinthe
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
        Fonction qui renvoie un dictionnaire composée des position des cellule adjacente a la position donnée en
        paramètre

        PRE : xMax et yMax doivent être des INT

        POST : renvoie un dictionnaire composé de tout les positions des cellules adjacentes
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
    """class qui génère tout le labyrinthe de façon aléatoire"""

    def __init__(self, height=3, width=3):
        """
        PRE : height et width doivent être un INT

        POST : Initialise l'objet Labyrinthe
            height prend comme valeur le paramètre height
            width prend comme valeur le paramètre width
            start prend comme valeur {"x":None,"y":None}
            end prend comme valeur {"x":None,"y":None}
            laby prend comme valeur []
            wall prend comme valeur []
            item prend comme valeur []
            mobs prend comme valeur []
        """
        self.__height = round(height)  # hauteur du Labyrinthe
        self.__width = round(width)  # largeur du Labyrinthe
        self.start = {"x": None, "y": None}  # position du debut
        self.end = {"x": None, "y": None}  # position de la fin
        self.laby = []  # tableau qui sera compose de tout les cellule du Labyrinthe
        self.wall = []  # tableau qui sera compose de tout les murs du Labyrinthe
        self.item = []
        self.mobs = []
        self.build_grid()  # creation de tout les cellule
        self.build_way()  # creation du chemin grace a l'algorithme
        self.start_and_end()  # positionnement du debut e de la fin

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def get_cell(self, x, y):
        """
        fonction qui permet d'obtenir la cellule via c'est coordonnée

        PRE : x et y doivent être des int

        POST : renvoie la cellule sélectionnée
        """
        return self.laby[y][x]

    def build_grid(self):
        """
        fonction qui cree toute les cellule du Labyrinthe

        PRE : -

        POST : construit la grille du labyrinthe
            ajout de la variable laby un objet Cell
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
                            y != line * 2):  # vrai que si les cellule sont des mur intérieur (pas les mur qui sont
                        # le  contour du Labyrinthe)
                        if not (x % 2 == 0 and y % 2 == 0):
                            self.wall.append(
                                self.laby[y][-1].id)  # ajoute de id de cellule qui sont des mur dans la variable wall
                else:
                    self.laby[y].append(Cell(x, y))  # ajout de la cellule dans la variable laby

    def build_way(self):
        """fonction qui, via l'algorithme de creation de chemin, vas cree le chemin aléatoirement

        PRE : -

        POST : construit le chemin du labyrinthe
            modifie tout les cellules dans le labyrinthe
        """
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
                vRight = self.get_cell(**dic["right"]).numb
                vLeft = self.get_cell(**dic["left"]).numb
                if not (vRight == vLeft):
                    cell.wall = False
                    if (vRight > vLeft):
                        self.new_val(vRight, vLeft)
                    else:
                        self.new_val(vLeft, vRight)
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

        PRE : val et nVal doivent être des int

        POST : remplace tout les valeurs des cellule sélectionnées par la nouvelle valeur
            modifie la valeur numb de la cellule sélectionnée par nVal
        """
        for y in self.laby:
            for x in y:
                if x.numb == val:
                    x.numb = nVal

    def val_verif(self):
        """fonction qui verifies si la valeur de 2 cellule sont les meme

        PRE : -

        POST : renvoie True si une valeur dans le labyrinthe est différente de 0 ou -1, sinon renvoie False
        """
        for y in self.laby:
            for x in y:
                if x.numb != 0 or x.numb != -1:
                    return True
        return False

    def hero_move(self, lastx, lasty, newx, newy):
        """
        fonction qui vas permettre de changer la position du hero en changeant la valeur hero dans les cellules

        PRE : lastx, lasty, newx, newy doivent être des int

        POST : modifie les cellules sélectionnées en remplacent la valeur hero des cellules
        """
        self.get_cell(lastx, lasty).hero = False
        self.get_cell(newx, newy).hero = True

    def pop_hero(self):
        """fonction qui ajoute le hero dans le labyrinthe a la position voulu

        PRE : -

        POST : ajoute le hero dans la cellule sélectionnée en modifiant la variable hero
        """
        self.get_cell(**self.start).hero = True

    def start_and_end(self):
        """fonction qui vas générer le debut et la fin du labyrinthe aléatoirement

        PRE : -

        POST : attribue les coordonnées du debut et de la fin
        """
        listOfCell = []
        for y in self.laby:
            for x in y:
                if not x.wall:
                    listOfCell.append(x)
        # génère un nombre aléatoire entre 0 et la longueur max du tableau listOfCell
        rand = random.randrange(0, len(listOfCell))
        celluleRandom = listOfCell[rand]  # sélectionne l objet dans le tableau
        self.set_start(celluleRandom.x, celluleRandom.y)  # attribut les valeur x et y a start
        del celluleRandom  # retire la cellule du tableau pour ne pas la réutiliser
        # génère un nombre aléatoire entre 0 et la longueur max du tableau listOfCell
        rand = random.randrange(0, len(listOfCell))
        celluleRandom = listOfCell[rand]  # sélectionne l objet dans le tableau
        celluleRandom.end = True
        self.set_end(celluleRandom.x, celluleRandom.y)  # attribut les valeur x et y a end
        self.pop_hero()  # appel la fonction pop_hero()

    def set_start(self, x, y):
        """
        cree le dictionnaire qui sera introduit dans la variable start

        PRE : x et y doivent être un int

        POST : crée de dictionnaire de coordonnée du start
            attribut le dictionnaire crée a la variable start
        """
        self.start = {"x": x, "y": y}

    def set_end(self, x, y):
        """
        cree le dictionnaire qui sera introduit dans la variable end
            attribut le dictionnaire crée a la variable end

        PRE : x et y doivent être un int

        POST : crée de dictionnaire de coordonnée du end
        """
        self.end = {"x": x, "y": y}

    def add_item(self, listOfItem):
        """fonction dui ajoute un ou des items dans le labyrinthe

        PRE : liste des item a rajouter sous forme ("nomDeObjet", "NomVariablePhoto")

        POST : ajoute a la list des item les different objet et leur attribut une position (deux objet n ont pas la
        meme position)
        """
        listOfCell = []
        for y in self.laby:
            for x in y:
                if not x.wall and not x.end and not x.hero:
                    listOfCell.append(x)
        for i in listOfItem:
            rand = random.randrange(0, len(listOfCell))
            cellRand = listOfCell[rand]
            self.item.append(Item(cellRand.x, cellRand.y, i[0], i[1]))
            del listOfCell[rand]

    def del_item(self, x, y):
        """
        fonction qui supprime un objet du labyrinthe

        PRE : x et y doivent être un int

        POST : supprime un objet en fonction de sa position et renvoie l'item supprimé
        """
        listItem = list(map(lambda x: x.id, self.item))
        id = "{},{}".format(x, y)
        if id in listItem:
            index = listItem.index(id)
            item = self.item[index]
            del self.item[index]
            return item

    def add_mobs(self, listOfMobs):
        """
        fonction qui ajoute les monstres dans le labyrinthe

        PRE : liste des mobs a rajouter sous forme ("couleur", "type", vie)

        POST : ajoute a la list des mobs les different monstre et leur attribut une position
        """
        listOfCell = []
        for y in self.laby:
            for x in y:
                if not x.wall and not x.end and not x.hero:
                    listOfCell.append(x)
        for i in listOfMobs:
            rand = random.randrange(0, len(listOfCell))
            cellRand = listOfCell[rand]
            mobs = Monstre()
            mobs.setPosi(cellRand.x, cellRand.y)
            mobs.color = i[0]
            mobs.typeMonstre = i[1]
            mobs.life = i[2]
            self.mobs.append(mobs)
            del listOfCell[rand]

    def del_mobs(self, x, y):
        """
        fonction qui supprime un objet du labyrinthe

        PRE : x et y doivent être un int

        POST : supprime un monstre en fonction de sa position et renvoie le monstre supprimé
        """
        listMobs = list(map(lambda x: x.id, self.mobs))
        id = "{},{}".format(x, y)
        if id in listMobs:
            index = listMobs.index(id)
            mobs = self.mobs[index]
            del self.mobs[index]
            return mobs

    def exist_item(self, x, y):
        """
        verifie si l'item existe

        PRE :x et y doivent être un int

        POST : renvoie True si l'objet exist, sinon renvoie False
        """
        listItem = list(map(lambda x: x.id, self.item))
        id = "{},{}".format(x, y)
        return id in listItem

    def exist_mobs(self, x, y):
        """
        verifie si le monstre existe

        PRE :x et y doivent être un int

        POST : renvoie True si le monstre exist, sinon renvoie False
        """
        listmobs = list(map(lambda x: x.id, self.mobs))
        id = "{},{}".format(x, y)
        return id in listmobs

    def show(self):
        """permet de montrer le labyrinthe en

        PRE : -

        POST : permet d'afficher le labyrinthe en console"""
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
        fonction qui return les positions des différentes mur qu'il y a autour de la cellules

        PRE : x et y doivent être des int:

        POST : renvoi un list de tout les murs autour d'une cellule sélectionnée:
        """
        list = []
        dic = self.get_cell(x, y).cell_adj(self.width, self.height)
        for i in dic:
            if self.get_cell(**dic[i]).wall:
                list.append(i)
        return list



if __name__ == "__main__":
    l = Labyrinthe(3, 6)
    l.show()
