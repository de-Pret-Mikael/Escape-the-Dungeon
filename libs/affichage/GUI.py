from random import randrange

import pygame
from pygame.locals import *
from PIL import ImageTk, Image
from libs.labyrinthe import Labyrinthe
from libs.hero import Hero
from libs.photo import Photo


class Gui:
    def __init__(self):
        self.laby = None
        self.hero = Hero()
        self.pPng = None
        self.pDun = None
        self.pKey = None
        self.ecran = None
        self.continue_acceuil = True
        self.continue_jeu = True

    @property
    def start(self):
        return self.laby.start

    @property
    def item(self):
        return self.laby.item

    @property
    def hx(self):
        return self.hero.x

    @property
    def hy(self):
        return self.hero.y

    def screen_set_mode(self, height, width, size):
        self.ecran = pygame.display.set_mode(((width * 2 + 1) * size, (height * 2 + 1) * size))

    def update_photo(self, name, path, sizeTup):
        if name in self.__dict__:
            self.__dict__[name] = Photo(path, sizeTup)

    def update_all_photo(self, tupSize):
        self.update_photo("pDun", "img/dungeon", tupSize)
        self.update_photo("pPng", "img/player/{}".format(self.hero.color), tupSize)
        self.update_photo("pKey", "img/key", tupSize)

    def interDungeon(self, size, width, height, pDun):
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
        dungeon.save("img/floor/floor.jpeg")

    def interHero(self, size, pPng):
        hero = Image.new("RGBA", (size, size))
        if self.hero.soldier:
            hero.paste(pPng.soldier, (0, 0))
        else:
            hero.paste(pPng.mage, (0, 0))

        hero.save("img/floor/hero.png")

    def interItem(self, size, pItem, name):
        items = Image.new("RGBA", (size, size))
        items.paste(self.__dict__[pItem].__dict__[name], (0, 0))
        items.save("img/floor/{}.png".format(name))

    def new_dungeon(self, height, width, size, item):
        tupSize = (size, size)
        self.update_all_photo(tupSize)
        self.laby = Labyrinthe(height, width)
        self.hero.setPosi(**self.laby.start)
        self.laby.add_item(item)
        self.interHero(size, self.pPng)
        self.interDungeon(size, width, height, self.pDun)
        for i in self.item:
            self.interItem(size, i.pType, i.itemName)

    def init_build(self, height, width, size, listOfItem):
        tupSize = (size, size)
        self.continue_acceuil = False
        self.update_all_photo(tupSize)
        self.new_dungeon(height, width, size, listOfItem)
