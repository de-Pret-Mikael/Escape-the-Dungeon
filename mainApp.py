from random import randrange

import pygame
from pygame.locals import *
from PIL import ImageTk, Image
from libs.labyrinthe import Labyrinthe
from libs.hero import Hero
from libs.photo import Photo


# import sys


def interDungeon(size, width, height, laby, pDun):
    img_w = (width * 2 + 1) * size
    img_h = (height * 2 + 1) * size
    dungeon = Image.new("RGB", (img_w, img_h))
    for y in laby.laby:
        for x in y:
            xImg = x.x * size
            yImg = x.y * size
            if x.wall:
                list = laby.wall_around(x.x, x.y)
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
                if laby.get_cell(x.x, x.y).end:
                    dungeon.paste(pDun.trap, (xImg, yImg))
    dungeon.save("img/floor/floor.jpeg")


def interHero(size, pPng, soldier=True):
    hero = Image.new("RGBA", (size, size))
    if soldier:
        hero.paste(pPng.soldier, (0, 0))
    else:
        hero.paste(pPng.mage, (0, 0))

    hero.save("img/floor/hero.png")


def interItem(x, y, size, pItem, name):
    items = Image.new("RGBA", (size, size))
    items.paste(pItem.__dict__[name], (x, y))
    items.save("img/floor/{}.png".format(name))


def new_tail(heigth, width, size, item):
    laby.__init__(heigth, width)
    hero.setPosi(**laby.start)
    laby.add_item(item)
    interHero(size, pPng, soldier=True)
    interDungeon(size, width, height, laby, pDun)
    for i in laby.item:
        interItem(i.x, i.y, size, i.pType, i.itemName)


if __name__ == '__main__':
    height, width = 5, 5
    size = 32
    laby = Labyrinthe(height, width)
    hero = Hero()
    hero.setPosi(**laby.start)
    pDun = None
    pPng = None
    pKey = None
    pygame.init()

    conti = True

    ecran = pygame.display.set_mode(((width * 2 + 1) * size, (height * 2 + 1) * size))
    pygame.display.set_caption('Escape teh Donjon')
    while conti:

        acceuil = pygame.image.load("img/acceuil/acceuil.jpg").convert()
        ecran.blit(acceuil, (0, 0))

        pygame.display.flip()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                conti = False

        continue_acceuil = True
        continue_jeu = True
        save_K = ''
        path_hero = "img/player/blue"
        path_key = "img/key"
        while continue_acceuil:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    height, width, size = 5, 5, 32
                    ecran = pygame.display.set_mode(((width * 2 + 1) * size, (height * 2 + 1) * size))
                    continue_acceuil = False
                    continue_jeu = False
                    conti = False


                elif event.type == KEYDOWN:
                    if event.key == K_F1:
                        height, width, size = 10, 10, 32
                        ecran = pygame.display.set_mode(((width * 2 + 1) * size, (height * 2 + 1) * size))
                        continue_acceuil = False
                        save_K = 'K_F1'
                        pDun = Photo("img/dungeon", (size, size))
                        pPng = Photo(path_hero, (size, size))
                        pKey = Photo(path_key, (size, size))
                        listOfItem = {"clebronze": pKey}
                        new_tail(height, width, size, listOfItem)


                    elif event.key == K_F2:
                        height, width, size = 15, 20, 25
                        ecran = pygame.display.set_mode(((width * 2 + 1) * size, (height * 2 + 1) * size))
                        continue_acceuil = False
                        save_K = 'K_F2'
                        pDun = Photo("img/dungeon", (size, size))
                        pPng = Photo(path_hero, (size, size))
                        pKey = Photo(path_key, (size, size))
                        listOfItem = {"clebronze": pKey}
                        new_tail(height, width, size, listOfItem)

                    elif event.key == K_F3:
                        height, width, size = 20, 30, 16
                        ecran = pygame.display.set_mode(((width * 2 + 1) * size, (height * 2 + 1) * size))
                        continue_acceuil = False
                        save_K = 'K_F3'
                        pDun = Photo("img/dungeon", (size, size))
                        pPng = Photo(path_hero, (size, size))
                        pKey = Photo(path_key, (size, size))
                        listOfItem = {"clebronze": pKey}
                        new_tail(height, width, size, listOfItem)

                    elif event.key == K_F4:
                        height, width, size = 30, 40, 16
                        ecran = pygame.display.set_mode(((width * 2 + 1) * size, (height * 2 + 1) * size))
                        continue_acceuil = False
                        save_K = 'K_F4'
                        pDun = Photo("img/dungeon", (size, size))
                        pPng = Photo(path_hero, (size, size))
                        pKey = Photo(path_key, (size, size))
                        listOfItem = {"clebronze": pKey}
                        new_tail(height, width, size, listOfItem)

                    elif event.key == K_F5:
                        height, width, size = 30, 60, 15
                        ecran = pygame.display.set_mode(((width * 2 + 1) * size, (height * 2 + 1) * size))
                        continue_acceuil = False
                        save_K = 'K_F5'
                        pDun = Photo("img/dungeon", (size, size))
                        pPng = Photo(path_hero, (size, size))
                        pKey = Photo(path_key, (size, size))
                        listOfItem = {"clebronze": pKey}
                        new_tail(height, width, size, listOfItem)

                    elif event.key == K_F6:
                        event.key = save_K
                        continue_acceuil = False

        while continue_jeu:
            pos_peso = laby.start
            perso = pygame.image.load("img/floor/hero.png").convert_alpha()
            position_perso = perso.get_rect()
            hx = hero.x * size
            hy = hero.y * size
            ecran.blit(perso, (hx, hy, hx + size, hy + size))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continue_jeu = False
                    if event.key == K_DOWN:
                        hero.bas(laby)
                    if event.key == K_UP:
                        hero.haut(laby)
                    if event.key == K_RIGHT:
                        hero.droite(laby)
                    if event.key == K_LEFT:
                        hero.gauche(laby)
                    if event.key == K_e and hero.end(**laby.end):
                        hero.end(**laby.end)
                        continue_jeu = False

                if event.type == pygame.QUIT:
                    continue_jeu = False
                    conti = False

            fond = pygame.image.load("img/floor/floor.jpeg")
            pygame.display.set_icon(fond)
            pygame.display.flip()
            ecran.blit(fond, (0, 0))
        ecran.blit(acceuil, (0, 0))
        ecran.blit(perso, position_perso)
        pygame.display.flip()
