from random import randrange

import pygame
from pygame.locals import *
from PIL import ImageTk, Image
from libs.labyrinthe import Labyrinthe
from libs.hero import Hero
from libs.photo import Photo
from libs.affichage import *

# import sys
if __name__ == '__main__':
    gui = Gui()
    height, width = 5, 5
    size = 32
    conti = True
    gui.screen_set_mode(height, width, size)
    pygame.display.set_caption('Escape teh Donjon')
    while conti:
        acceuil = pygame.image.load("img/acceuil/acceuil.jpg").convert()
        gui.ecran.blit(acceuil, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                conti = False
        gui.continue_acceuil = True
        gui.continue_jeu = True
        while gui.continue_acceuil:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    height, width, size = 5, 5, 32
                    gui.screen_set_mode(height, width, size)
                    gui.continue_acceuil = False
                    gui.continue_jeu = False
                    conti = False


                elif event.type == KEYDOWN:
                    if event.key == K_F1:
                        height, width, size = 10, 10, 32
                        gui.screen_set_mode(height, width, size)
                        listOfItem = [("clebronze", "pKey"), ("clegold", "pKey")]
                        gui.init_build(height, width, size, listOfItem)


                    elif event.key == K_F2:
                        height, width, size = 15, 20, 25
                        gui.screen_set_mode(height, width, size)
                        listOfItem = [("clebronze", "pKey"), ("clegold", "pKey")]
                        gui.init_build(height, width, size, listOfItem)

                    elif event.key == K_F3:
                        height, width, size = 20, 30, 16
                        gui.screen_set_mode(height, width, size)
                        listOfItem = [("clebronze", "pKey"), ("clegold", "pKey")]
                        gui.init_build(height, width, size, listOfItem)

                    elif event.key == K_F4:
                        height, width, size = 30, 40, 16
                        gui.screen_set_mode(height, width, size)
                        listOfItem = [("clebronze", "pKey"), ("clegold", "pKey")]
                        gui.init_build(height, width, size, listOfItem)

                    elif event.key == K_F5:
                        height, width, size = 30, 60, 15
                        gui.screen_set_mode(height, width, size)
                        listOfItem = [("clebronze", "pKey"), ("clegold", "pKey")]
                        gui.init_build(height, width, size, listOfItem)

                    elif event.key == K_F6:
                        gui.continue_acceuil = False
                        print("coucou")

        while gui.continue_jeu:
            pos_peso = gui.start
            perso = pygame.image.load("img/floor/hero.png").convert_alpha()
            position_perso = perso.get_rect()
            hx = gui.hx * size
            hy = gui.hy * size
            gui.ecran.blit(perso, (hx, hy, hx + size, hy + size))
            for i in gui.item:
                gui.interItem(size, i.pType, i.itemName)
                item = pygame.image.load("img/floor/{}.png".format(i.itemName))
                ix = i.x * size
                iy = i.y * size
                gui.ecran.blit(item, (ix, iy, ix + size, iy + size))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        gui.continue_jeu = False
                    if event.key == K_DOWN:
                        gui.hero.bas(gui.laby)
                    if event.key == K_UP:
                        gui.hero.haut(gui.laby)
                    if event.key == K_RIGHT:
                        gui.hero.droite(gui.laby)
                    if event.key == K_LEFT:
                        gui.hero.gauche(gui.laby)
                    if event.key == K_e and gui.hero.end(**gui.laby.end):
                        gui.hero.end(**gui.laby.end)
                        gui.continue_jeu = False

                if event.type == pygame.QUIT:
                    gui.continue_jeu = False
                    conti = False

            fond = pygame.image.load("img/floor/floor.jpeg")
            pygame.display.set_icon(fond)
            pygame.display.flip()
            gui.ecran.blit(fond, (0, 0))
        gui.ecran.blit(acceuil, (0, 0))
        gui.ecran.blit(perso, position_perso)
        pygame.display.flip()
