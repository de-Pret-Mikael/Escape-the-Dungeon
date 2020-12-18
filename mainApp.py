import pygame
import pygame_menu
from pygame.locals import *
from libs.affichage.GUI import Gui
from libs.labyrinthe import Labyrinthe


def menu():
    height, width, size = 10, 10, 32
    gui.screen_set_mode(height, width, size)
    menu = pygame_menu.Menu(500, 500, 'Escape the Donjon',
                            theme=pygame_menu.themes.THEME_BLUE)
    menu.add_text_input('Name : ', default='Player', onchange=gui.set_name, maxchar=15)
    menu.add_selector('Difficulty :', [('easy', 1), ('moins easy', 2), ('pas easy', 3), ('shit', 4), ('shiit', 5)],
                      onchange=gui.set_difficulty)
    menu.add_selector('character', [('soldier', 1), ('mage', 2)], onchange=gui.set_hero)
    menu.add_button('Play', menu.disable)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(gui.ecran)

if __name__ == '__main__':
    pygame.init()
    gui = Gui()
    laby = Labyrinthe()
    menu()
    # score()
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
        gui.menu = True
        gui.continue_jeu = True
        while gui.menu:
            green_ork_1 = ("green", "ork1", 2)
            blue_ork_1 = ("blue", "ork1", 2)
            red_ork_1 = ("red", "ork1", 2)
            green_ork_2 = ("green", "ork2", 4)
            blue_ork_2 = ("blue", "ork2", 4)
            red_ork_2 = ("red", "ork2", 4)
            green_slime_1 = ("green", "slime1", 1)
            blue_slime_1 = ("blue", "slime1", 1)
            red_slime_1 = ("red", "slime1", 1)
            green_slime_2 = ("green", "slime2", 2)
            blue_slime_2 = ("blue", "slime2", 2)
            red_slime_2 = ("red", "slime2", 2)
            green_slime_3 = ("green", "slime3", 3)
            blue_slime_3 = ("blue", "slime3", 3)
            red_slime_3 = ("red", "slime3", 3)

            if gui.difficulty == K_F1:
                height, width, size = 5, 5, 48
                gui.screen_set_mode(height, width, size)
                listOfItem = [("clebronze", "pKey")]
                listOfMobs = [green_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1, blue_ork_1, red_ork_1]
                gui.init_build(height, width, size, listOfItem, listOfMobs)

            elif gui.difficulty == K_F2:
                height, width, size = 15, 20, 30
                gui.screen_set_mode(height, width, size)
                listOfItem = [("clebronze", "pKey"), ("cleargent", "pKey")]
                listOfMobs = [blue_ork_1, green_slime_2, red_slime_1]
                gui.init_build(height, width, size, listOfItem, listOfMobs)

            elif gui.difficulty == K_F3:
                height, width, size = 20, 30, 23
                gui.screen_set_mode(height, width, size)
                listOfItem = [("cleargent", "pKey"), ("clegold", "pKey")]
                listOfMobs = [blue_slime_3, green_slime_2, red_ork_2]
                gui.init_build(height, width, size, listOfItem, listOfMobs)

            elif gui.difficulty == K_F4:
                height, width, size = 30, 40, 16
                gui.screen_set_mode(height, width, size)
                listOfItem = [("clebronze", "pKey"), ("cleargent", "pKey"), ("clegold", "pKey")]
                listOfMobs = [blue_slime_3, red_ork_2, green_slime_3]
                gui.init_build(height, width, size, listOfItem, listOfMobs)


            elif gui.difficulty == K_F5:
                height, width, size = 30, 60, 15
                gui.screen_set_mode(height, width, size)
                listOfItem = [("clebronze", "pKey"), ("cleargent", "pKey"), ("clegold", "pKey"), ("cleargent", "pKey"), ("clegold", "pKey"), ("cleargent", "pKey"), ("clegold", "pKey"), ("cleargent", "pKey"), ("clegold", "pKey"), ("cleargent", "pKey"), ("clegold", "pKey")]
                listOfMobs = []
                for i in range(0, 3000):
                    listOfMobs.append(green_slime_2)
                print(len(listOfMobs))
                gui.init_build(height, width, size, listOfItem, listOfMobs)
            for event in pygame.event.get():
                if event.type == QUIT:
                    height, width, size = 5, 5, 32
                    gui.screen_set_mode(height, width, size)
                    gui.menu = False
                    gui.continue_jeu = False
                    conti = False

        while gui.continue_jeu:
            gui.affiche_perso(size)
            gui.affiche_item(size)
            gui.affiche_mobs(size)
            for event in pygame.event.get():
                #pygame.key.set_repeat(150, 30)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        gui.continue_jeu = False
                        gui.menu = True
                    if event.key == K_DOWN:
                        gui.depl_mobs()
                        gui.hero.move_bas(gui.laby)
                    if event.key == K_UP:
                        gui.depl_mobs()
                        gui.hero.move_haut(gui.laby)
                    if event.key == K_RIGHT:
                        gui.depl_mobs()
                        gui.hero.move_droite(gui.laby)
                    if event.key == K_LEFT:
                        gui.depl_mobs()
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

            fond = pygame.image.load("img/floor/floor.png")
            pygame.display.set_icon(fond)
            pygame.display.flip()
            gui.ecran.blit(fond, (0, 0))
        # gui.ecran.blit(acceuil, (0, 0))
        pygame.display.flip()
