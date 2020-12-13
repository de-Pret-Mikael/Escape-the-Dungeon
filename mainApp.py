from random import randrange

import pygame
from pygame.locals import *
import pygame_menu
from PIL import ImageTk, Image
from libs.labyrinthe import Labyrinthe
from libs.hero import Hero
from libs.photo import Photo
from libs.affichage import *


def menu():
    height, width, size = 10, 10, 32
    gui.screen_set_mode(height, width, size)
    menu = pygame_menu.Menu(300, 400, 'Escape the Donjon',
                            theme=pygame_menu.themes.THEME_BLUE)
    # gui.ecran.blit(acceuil, (0, 0))
    menu.add_selector('Difficulty :', [('easy', 1), ('moins easy', 2), ('pas easy', 3), ('shit', 4), ('shiit', 5)],
                      onchange=gui.set_difficulty)
    menu.add_selector('personnage', [('guerier', 1), ('mage', 2)], onchange=gui.set_hero)
    menu.add_button('Play', menu.disable)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(gui.ecran)

    # import sys


if __name__ == '__main__':
    pygame.init()
    gui = Gui()
    menu()
    gui.start_the_game()
    height, width = 5, 5
    size = 32
    conti = True
    gui.screen_set_mode(height, width, size)
    pygame.display.set_caption('Escape the Donjon')
    while conti:
        # acceuil = pygame.image.load("img/acceuil/acceuil.jpg").convert()

        # gui.ecran.blit(acceuil, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                conti = False
        gui.continue_acceuil = True
        gui.continue_jeu = True
        while gui.continue_acceuil:
            if gui.difficulty == K_F1:
                height, width, size = 10, 10, 32
                gui.screen_set_mode(height, width, size)
                listOfItem = [("clebronze", "pKey")]
                gui.init_build(height, width, size, listOfItem)

            elif gui.difficulty == K_F2:
                height, width, size = 15, 20, 30
                gui.screen_set_mode(height, width, size)
                listOfItem = [("clebronze", "pKey"), ("cleargent", "pKey")]
                gui.init_build(height, width, size, listOfItem)

            elif gui.difficulty == K_F3:
                height, width, size = 20, 30, 23
                gui.screen_set_mode(height, width, size)
                listOfItem = [("cleargent", "pKey"), ("clegold", "pKey")]
                gui.init_build(height, width, size, listOfItem)

            elif gui.difficulty == K_F4:
                height, width, size = 30, 40, 16
                gui.screen_set_mode(height, width, size)
                listOfItem = [("clebronze", "pKey"), ("cleargent", "pKey"), ("clegold", "pKey")]
                gui.init_build(height, width, size, listOfItem)

            elif gui.difficulty == K_F5:
                height, width, size = 30, 60, 15
                gui.screen_set_mode(height, width, size)
                listOfItem = [("clebronze", "pKey"), ("cleargent", "pKey"), ("clegold", "pKey"),
                              ("dieu", "pKey")]
                gui.init_build(height, width, size, listOfItem)
            for event in pygame.event.get():
                if event.type == QUIT:
                    height, width, size = 5, 5, 32
                    gui.screen_set_mode(height, width, size)
                    gui.continue_acceuil = False
                    gui.continue_jeu = False
                    conti = False

        while gui.continue_jeu:
            pos_peso = gui.start
            perso = pygame.image.load("img/floor/hero.png")
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
                pygame.key.set_repeat(150, 30)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        gui.continue_jeu = False
                    if event.key == K_DOWN:
                        gui.hero.move_bas(gui.laby)
                    if event.key == K_UP:
                        gui.hero.move_haut(gui.laby)
                    if event.key == K_RIGHT:
                        gui.hero.move_droite(gui.laby)
                    if event.key == K_LEFT:
                        gui.hero.move_gauche(gui.laby)
                    if event.key == K_e:
                        if gui.hero.end(**gui.laby.end):
                            gui.hero.end(**gui.laby.end)
                            gui.continue_jeu = False
                        if gui.laby.exist_item(gui.hx, gui.hy):
                            items = gui.laby.del_item(gui.hx, gui.hy)
                            gui.hero.add_inventaire(items)

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
