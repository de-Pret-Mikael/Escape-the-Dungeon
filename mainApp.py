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


if __name__ == '__main__':
    height, width = 5, 5
    size = 32
    laby = Labyrinthe(height, width)
    hero = Hero()
    pDun = Photo("img/dungeon", (size, size))
    pPng = Photo("img/player/blue", (size, size))
    interDungeon(size, width, height, laby, pDun)
    pygame.init()

    ecran = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Escape teh Donjon')
    acceuil = pygame.image.load("img/acceuil/acceuil.jpg").convert()
    ecran.blit(acceuil, (0, 0))

    perso = pygame.image.load("img/player/blue/mage.png").convert_alpha()
    position_perso = perso.get_rect()
    ecran.blit(perso, position_perso)

    conti = True
    while conti:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                conti = False
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    position_perso = position_perso.move(0, 6)
                if event.key == K_UP:
                    position_perso = position_perso.move(0, -6)
                if event.key == K_RIGHT:
                    position_perso = position_perso.move(6, 0)
                if event.key == K_LEFT:
                    position_perso = position_perso.move(-6, 0)

        ecran.blit(acceuil, (0, 0))
        ecran.blit(perso, position_perso)
        pygame.display.flip()
"""


def interHero(app, hero, pPng, soldier=True):
    xCan = hero.x * size +2
    yCan = hero.y * size +2
    if soldier:
        app.draw_img(xCan, yCan, anchor="nw", img=pPng.soldier)
    else:
        app.draw_img(xCan, yCan, anchor="nw", img=pPng.mage)

def move(event):
    l = event.widget.laby
    png = event.widget.hero
    if event.char == "e" and (l.end == {"x": png.x, "y": png.y}):
        myapp.quit()
        print("vous avez trouver la sortie")
    png.move(event.char,laby=l)
    heroPos = {"lastx": png.lastx, "lasty": png.lasty, "newx": png.x, "newy": png.y}
    l.heroMove(**heroPos)
    myapp.update_can(anchor="nw")
    interHero(myapp, png, pPng,soldier=False)
    myapp.update()

def new():
    myapp.laby = Labyrinthe(height, width)
    l = myapp.laby
    png = myapp.hero
    png.setPosi(**l.start)
    myapp.save_can(interDungeon(size, width, height, l, pDun))
    myapp.update_can(anchor="nw")
    interHero(myapp, png, pPng,soldier=False)
    myapp.update()
    pass

if __name__ == "__main__":
    height, width = 5,5
    size = 32
    # application
    name = "students's dungeon"
    minsize = ((width * 2 + 1) * size, (height * 2 + 1) * size)
    myapp = App(title=name, minSize=minsize, laby=Labyrinthe(height, width), hero=Hero())
    myapp.build_can(height=(height * 2 + 1) * size - 2, width=(width * 2 + 1) * size - 2, bg="black")
    # image
    pDun = Photo("img/dungeon", (size, size))
    pPng = Photo("img/player/blue", (size, size), photo=True)
    # menu
    mainmenu = tkinter.Menu(myapp)

    first_menu = tkinter.Menu(mainmenu, tearoff=0)
    first_menu.add_command(label="new", command=new)
    first_menu.add_command(label="quitter", command=myapp.quit)

    second_menu = tkinter.Menu(mainmenu,tearoff=0)
    second_menu.add_command(label="commande")



    mainmenu.add_cascade(label="jeu", menu=first_menu)
    mainmenu.add_cascade(label="option", menu=second_menu)
    myapp.configure(menu=mainmenu)
    tupleSequence = ("<KeyPress-z>", "<KeyPress-q>", "<KeyPress-s>", "<KeyPress-d>", "<KeyPress-e>")
    myapp.event_add("<<move>>", *tupleSequence)
    myapp.add_bind("<<move>>", move)
    myapp.launch()
    """
# myapp.resizable(width=False,height=False)
"""
def afficher():
    pygame.init()
    fenetre = pygame.display.set_mode((600, 400))


    perso = pygame.image.load("img/player/blue/mage.png")
    pygame.display.set_icon(perso)

    pygame.display.set_caption("Escape the Donjon")

    conti = True
    while conti:
        acceuil = pygame.image.load("img/acceuil/acceuil.jpg").convert()
        fenetre.blit(acceuil, (0, 0))

        pygame.display.flip()

        continue_jeu = True
        continue_acceuil = True

        while continue_acceuil:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    continue_acceuil = False
                    continue_jeu = False
                    conti = False
                    choix_tail = 0

                elif event.type == KEYDOWN:
                    if event.key == K_F1:
                        continue_acceuil = 0
                        choix_tail = 1

                    elif event.key == K_F2:
                        continue_acceuil = 0
                        choix_tail = 2

                    elif event.key == K_F3:
                        continue_acceuil = 0
                        choix_tail = 3

                    elif event.key == K_F4:
                        continue_acceuil = 0
                        choix_tail = 4

        if choix_tail != 0:
            level."appel de la classe qui affiche le laby"
            level."appel fct pour generer"
            level."def afficher(fenetre)"


        while continue_jeu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continue_jeu = False
                    conti = False

                elif event.key == K_a:
                    Labyrinthe.heroMove('droite')
                elif event.key == K_d:
                    Labyrinthe.heroMove('gauche')
                elif event.key == K_s:
                    Labyrinthe.heroMove('bas')
                elif event.key == K_w:
                    Labyrinthe.heroMove('haut')

            fenetre.blit(fond, (0, 0))
            fond = pygame.image.load("img/floor/floor.jpeg")
            pygame.display.set_icon(fond)
            pygame.display.flip()

            if les coord de la sortiie:
                continue_jeu = 0
"""
