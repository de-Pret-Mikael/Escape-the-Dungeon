from random import randrange

import pygame
from pygame.locals import *
from PIL import Image
from libs.labyrinthe import Labyrinthe
from libs.hero import Hero
from libs.photo import Photo


class Gui:
    def __init__(self):
        """
        POST : donne la valeur None à laby, pPng, pDun, pKey, ecran, donne la valeur True à isSoldier, continue_jeu, menu, donne la class Hero à hero, met difficulty à K_F1, name à Player et score à 0
        """
        self.laby = None
        self.hero = Hero()
        self.pPng = None
        self.pDun = None
        self.pKey = None
        self.ecran = None
        self.isSoldier = True
        self.continue_jeu = True
        self.difficulty = K_F1
        self.menu = True
        self.name = "Player"
        self.score = 0

    @property
    def start(self):
        return self.laby.start

    @property
    def item(self):
        return self.laby.item

    @property
    def mobs(self):
        return self.laby.mobs

    @property
    def hx(self):
        return self.hero.x

    @property
    def hy(self):
        return self.hero.y

    def screen_set_mode(self, height, width, size):
        """
        PRE : height, width et size doivent être de type integer
        POST : Donne la taille de la fenetre
        """
        self.ecran = pygame.display.set_mode(((width * 2 + 1) * size, (height * 2 + 1) * size))

    def update_photo(self, name, path, sizeTup):
        """
        PRE : name, path doivent être de type str et sizeTup un tuple de type integer
        POST : donne le chemin et la taille de l'image
        """
        if name in self.__dict__:
            self.__dict__[name] = Photo(path, sizeTup)

    def update_all_photo(self, tupSize):
        """
        PRE : tupSize doit être un tuple de type integer
        POST : donne le chemin et la taille de l'image
        """
        self.update_photo("pDun", "img/dungeon", tupSize)
        self.update_photo("pPng", "img/player/{}".format(self.hero.color), tupSize)
        self.update_photo("pKey", "img/key", tupSize)

    def interDungeon(self, size, width, height, pDun):
        """
        PRE : size, width et height doivent être de type integer et pDun un object photo
        POST : Enregistre l'image construite du donjon dans le dossier img/floor
        """
        img_w = (width * 2 + 1) * size
        img_h = (height * 2 + 1) * size
        dungeon = Image.new("RGB", (img_w, img_h))
        for y in self.laby.laby:
            for x in y:
                xImg = x.x * size
                yImg = x.y * size
                if x.wall:
                    list = self.laby.wall_around(x.x, x.y)
                    top = "top" in list
                    down = "down" in list
                    left = "left" in list
                    right = "right" in list
                    if down and left and right:
                        dungeon.paste(pDun.wallT, (xImg, yImg))
                    elif down and left and top:
                        dungeon.paste(pDun.wallHR, (xImg, yImg))
                    elif down and right and top:
                        dungeon.paste(pDun.wallHL, (xImg, yImg))
                    elif right and left:
                        dungeon.paste(pDun.wallH, (xImg, yImg))
                    elif top and left:
                        dungeon.paste(pDun.wallDR, (xImg, yImg))
                    elif top and right:
                        dungeon.paste(pDun.wallDL, (xImg, yImg))
                    elif top and down:
                        dungeon.paste(pDun.wallV, (xImg, yImg))
                    elif down and left:
                        dungeon.paste(pDun.wallHR, (xImg, yImg))
                    elif down and right:
                        dungeon.paste(pDun.wallHL, (xImg, yImg))
                    elif top:
                        dungeon.paste(pDun.wallE, (xImg, yImg))
                    elif down:
                        dungeon.paste(pDun.wallV, (xImg, yImg))
                    elif left:
                        dungeon.paste(pDun.wallH, (xImg, yImg))
                    elif right:
                        dungeon.paste(pDun.wallH, (xImg, yImg))
                else:
                    rand = randrange(0, 2)
                    if rand:
                        dungeon.paste(pDun.ground1, (xImg, yImg))
                    else:
                        dungeon.paste(pDun.ground2, (xImg, yImg))
                    if self.laby.get_cell(x.x, x.y).end:
                        dungeon.paste(pDun.trap, (xImg, yImg))
        dungeon.save("img/floor/floor.png")

    def interHero(self, size, pPng):
        """
        PRE : size doit être de type integer et pPng doit être un object photo
        POST : permet d' enregistré l'image du soldat ou du mage dans le dossié img/floor
        """
        hero = Image.new("RGBA", (size, size))
        if self.hero.soldier:
            hero.paste(pPng.soldier, (0, 0))
        else:
            hero.paste(pPng.mage, (0, 0))

        hero.save("img/floor/hero.png")

    def interItem(self, size, pItem, name):
        """
        PRE : size doit être de type integer, pItem un object photo et name de type str
        POST : permet d' enregistré l'image de ou des item(s) dans le dossié img/floor
        """
        items = Image.new("RGBA", (size, size))
        items.paste(self.__dict__[pItem].__dict__[name], (0, 0))
        items.save("img/floor/{}.png".format(name))

    def interMobs(self, size, mobs):
        """
        PRE : size doit être de type integer et mobs un object photo
        POST : permet d' enregistré l'image de ou des mobs dans le dossié img/floor
        """
        sizetup = (size, size)
        pMobs = Photo(mobs.pathImg, sizetup)
        mobsImg = Image.new("RGBA", sizetup)
        mobsImg.paste(pMobs.__dict__[mobs.typeMonstre], (0, 0))
        mobsImg.save("img/floor/{}/{}.png".format(mobs.color, mobs.typeMonstre))

    def new_dungeon(self, height, width, size, item, listeNameMobs, dictMobs):
        """
        PRE : height, width, size doivent être de type integer et item doit être une liste de tuple composé de deux str et mobs une liste de tuple composé d'un integer et d'un str
        POST : donne la taille des images, la taille su labyrinthe, si c est un soldat ou un mage, la position de départ, place les items et les mobs
        """
        tupSize = (size, size)
        mobs = [dictMobs[i] for i in listeNameMobs]
        self.menu = False
        self.update_all_photo(tupSize)
        self.laby = Labyrinthe(height, width)
        self.hero = Hero()
        self.hero.soldier = self.isSoldier
        self.hero.setPosi(**self.start)
        self.laby.add_item(item)
        self.laby.add_mobs(mobs)
        self.interHero(size, self.pPng)
        self.interDungeon(size, width, height, self.pDun)
        for i in self.item:
            self.interItem(size, i.pType, i.itemName)
        for j in self.mobs:
            self.interMobs(size, j)


    def set_difficulty(self, difficulty, value):
        """
        PRE : value et difficulty doit être de type integer
        POST : Donne la valeur correspondante à difficulty
        """
        if value == 1:
            self.difficulty = K_F1
        if value == 2:
            self.difficulty = K_F2
        if value == 3:
            self.difficulty = K_F3
        if value == 4:
            self.difficulty = K_F4
        if value == 5:
            self.difficulty = K_F5

    def set_hero(self, hero, value):
        """
        PRE : hero doit être une liste et value est un integer
        POST : Permet de selectionner le soldier ou le mage
        """
        if hero[0] == "soldier":
            self.isSoldier = True
        else:
            self.isSoldier = False

    def start_the_game(self):
        """
        POST : Permet de quitter le menu et d'entré dans le jeu
        """
        self.menu = False
        self.continue_jeu = True

    def set_name(self, name):
        """
        PRE : name doit être de type str
        POST : enregistre le nom du joueur
        """
        self.name = name

    def affiche_item(self, size):
        """
        PRE : size doit être de type integer
        POST : Affiche les items dans le labyrinthe
        """
        for i in self.item:
            item = pygame.image.load("img/floor/{}.png".format(i.itemName))
            ix = i.x * size
            iy = i.y * size
            self.ecran.blit(item, (ix, iy, ix + size, iy + size))

    def affiche_perso(self, size):
        """
        PRE : size doit être de type integer
        POST : Affiche le personnage dans le labyrinthe
        """
        perso = pygame.image.load("img/floor/hero.png")
        hx = self.hx * size
        hy = self.hy * size
        self.ecran.blit(perso, (hx, hy, hx + size, hy + size))

    def affiche_mobs(self, size):
        """
        PRE : size doit être de type integer
        POST : Affiche les mobs dans le labyrinthe
        """
        for i in self.mobs:
            mobs = pygame.image.load("img/floor/{}/{}.png".format(i.color, i.typeMonstre))
            ix = i.x * size
            iy = i.y * size
            self.ecran.blit(mobs, (ix, iy, ix + size, iy + size))

    def depl_mobs(self):
        """
        POST : Permet de déplacer les mobs dans le labyrinthe
        """
        [x.deplacement(self.laby) for x in self.mobs]