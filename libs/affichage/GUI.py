from random import randrange

import pygame
from pygame.locals import *
from PIL import Image
from libs.labyrinthe import Labyrinthe
from libs.hero import Hero
from libs.photo import Photo

GREEN = (0, 190, 0)
ORANGE = (255, 165, 0)
ROUGE = (255, 69, 0)
MAUVE = (186, 99, 201)


class Gui:
    def __init__(self):
        """
        POST : donne la valeur None à laby, pPng, pDun, pKey, écran, donne la valeur True à isSoldier, continue_jeu,
        menu, donne la class Hero à hero, met difficulty à K_F1, name à Player et score à 0
        """
        self.laby = None
        self.hero = Hero()
        self.pPng = None
        self.pDun = None
        self.pKey = None
        self.ecran = None
        self.isSoldier = True
        self.continue_jeu = True
        self.game_over = False
        self.difficulty = K_F1
        self.menu = True
        self.name = "Player"
        self.pVie = None
        self.score = 0

    @property
    def start(self):
        return self.laby.start

    @property
    def end(self):
        return self.laby.end

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

    @property
    def hlx(self):
        return self.hero.lastx

    @property
    def hly(self):
        return self.hero.lasty

    def screen_set_mode(self, height, width, size):
        """
        PRE : height, width et size doivent être de type integer
        POST : Donne la taille de la fenêtre
        """
        self.ecran = pygame.display.set_mode(((width * 2 + 1) * size, (height * 2 + 1) * size))

    def update_photo(self, name, path, sizetup):
        """
        PRE : name, path doivent être de type str et sizeTup un tuple de type integer
        POST : donne le chemin et la taille de l'image
        """
        if name in self.__dict__:
            self.__dict__[name] = Photo(path, sizetup)

    def update_all_photo(self, tupsize):
        """
        PRE : tupSize doit être un tuple de type integer
        POST : donne le chemin et la taille de l'image
        """
        self.update_photo("pDun", "img/dungeon", tupsize)
        self.update_photo("pPng", "img/player/{}".format(self.hero.color), tupsize)
        self.update_photo("pKey", "img/key", tupsize)
        self.update_photo("pVie", "img/hearts", tupsize)

    def inter_dungeon(self, size, width, height):
        """
        PRE : size, width et height doivent être de type integer
        POST : Enregistre l'image construite du donjon dans le dossier img/floor
        """
        img_w = (width * 2 + 1) * size
        img_h = (height * 2 + 1) * size
        dungeon = Image.new("RGB", (img_w, img_h))
        for y in self.laby.laby:
            for x in y:
                x_img = x.x * size
                y_img = x.y * size
                if x.wall:
                    liste = self.laby.wall_around(x.x, x.y)
                    top = "top" in liste
                    down = "down" in liste
                    left = "left" in liste
                    right = "right" in liste
                    if down and left and right:
                        dungeon.paste(self.pDun.wallT, (x_img, y_img))
                    elif down and left and top:
                        dungeon.paste(self.pDun.wallHR, (x_img, y_img))
                    elif down and right and top:
                        dungeon.paste(self.pDun.wallHL, (x_img, y_img))
                    elif right and left:
                        dungeon.paste(self.pDun.wallH, (x_img, y_img))
                    elif top and left:
                        dungeon.paste(self.pDun.wallDR, (x_img, y_img))
                    elif top and right:
                        dungeon.paste(self.pDun.wallDL, (x_img, y_img))
                    elif top and down:
                        dungeon.paste(self.pDun.wallV, (x_img, y_img))
                    elif down and left:
                        dungeon.paste(self.pDun.wallHR, (x_img, y_img))
                    elif down and right:
                        dungeon.paste(self.pDun.wallHL, (x_img, y_img))
                    elif top:
                        dungeon.paste(self.pDun.wallE, (x_img, y_img))
                    elif down:
                        dungeon.paste(self.pDun.wallV, (x_img, y_img))
                    elif left:
                        dungeon.paste(self.pDun.wallH, (x_img, y_img))
                    elif right:
                        dungeon.paste(self.pDun.wallH, (x_img, y_img))
                else:
                    rand = randrange(0, 2)
                    if rand:
                        dungeon.paste(self.pDun.ground1, (x_img, y_img))
                    else:
                        dungeon.paste(self.pDun.ground2, (x_img, y_img))
                    if self.laby.get_cell(x.x, x.y).end:
                        dungeon.paste(self.pDun.trap, (x_img, y_img))
        dungeon.save("img/floor/floor.png", "PNG")

    def inter_hero(self, size):
        """
        PRE : size doit être de type integer
        POST : permet d' enregistré l'image du soldat ou du mage dans le dossier img/floor
        """
        hero = Image.new("RGBA", (size, size))

        if self.hero.soldier:
            hero.paste(self.pPng.soldier, (0, 0))
        else:
            hero.paste(self.pPng.mage, (0, 0))

        hero.save("img/floor/hero.png", "PNG")

    def inter_sang(self, size):
        """
        PRE : size doit être de type integer
        POST : permet d' enregistré l'image du soldat ou du mage dans le dossier img/floor
        """
        p_png = Photo("img/player/sang", (size, size))
        hero = Image.new("RGBA", (size, size))

        if self.hero.soldier:
            hero.paste(p_png.soldier, (0, 0))
        else:
            hero.paste(p_png.mage, (0, 0))

        hero.save("img/floor/Sang.png", "PNG")

    def inter_item(self, size, p_item, name):
        """
        PRE : size doit être de type integer, pItem un object photo et name de type str
        POST : permet d' enregistré l'image de ou des item(s) dans le dossier img/floor
        """
        items = Image.new("RGBA", (size, size))
        items.paste(self.__dict__[p_item].__dict__[name], (0, 0))
        items.save("img/floor/{}.png".format(name), "PNG")

    def inter_mobs(self, size, mobs):
        """
        PRE : size doit être de type integer et mobs un object photo
        POST : permet d' enregistré l'image de ou des mobs dans le dossier img/floor
        """
        sizetup = (size, size)
        p_mobs = Photo(mobs.path_img, sizetup)
        mobs_img = Image.new("RGBA", sizetup)
        mobs_img.paste(p_mobs.__dict__[mobs.typeMonstre], (0, 0))
        mobs_img.save("img/floor/{}/{}.png".format(mobs.color, mobs.typeMonstre), "PNG")

    def inter_vie(self, size):
        """
        PRE : size doit être de type integer
        POST : permet d' enregistré l'image de coeur dans le dossier img/floor
        """
        sizetup = (size, size)
        for i in self.pVie.__dict__:
            vie_img = Image.new("RGBA", sizetup)
            vie_img.paste(self.pVie.__dict__[i], (0, 0))
            vie_img.save("img/floor/{}.png".format(i), "PNG")

    def new_dungeon(self, height, width, size, item, liste_name_mobs, dict_mobs):
        """
        PRE : menu esr à False, height, width, size doivent être de type integer et item doit être une liste de tuple
        composé de deux str et listNameMobs une liste de string, dict_mobs est un dictionnaire POST : donne la taille
        des images, la taille su labyrinthe, si c est un soldat ou un mage, la position de départ, place les items et
        les mobs
        """
        tup_size = (size, size)
        mobs = [dict_mobs[i] for i in liste_name_mobs]
        self.menu = False
        self.update_all_photo(tup_size)
        self.laby = Labyrinthe(height, width)
        self.hero = Hero()
        self.hero.set_score(self.score)
        self.hero.soldier = self.isSoldier
        self.hero.set_posi(**self.start)
        self.laby.add_item(item)
        self.laby.add_mobs(mobs)
        self.inter_hero(size)
        self.inter_sang(size)
        self.inter_dungeon(size, width, height)
        self.inter_vie(size)
        for i in self.item:
            self.inter_item(size, i.pType, i.itemName)
        for j in self.mobs:
            self.inter_mobs(size, j)

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
        POST : Permet de sélectionner le soldier ou le mage
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
            item = pygame.image.load("./img/floor/{}.png".format(i.itemName))
            ix = i.x * size
            iy = i.y * size
            self.ecran.blit(item, (ix, iy, ix + size, iy + size))

    def affiche_perso(self, size):
        """
        PRE : size doit être de type integer
        POST : Affiche le personnage dans le labyrinthe
        """
        if self.hero.is_touche():
            path = "img/floor/Sang.png"
        else:
            path = "img/floor/hero.png"
        perso = pygame.image.load(path)
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

    def affiche_vie(self, size, width):
        """
        PRE : size doit être de type integer width doit être un integer
        POST : Affiche la vie en haut a droite dans le labyrinthe
        """
        vie_rouge = self.hero.vie
        width = width * 2
        for i in range(0, self.hero.maxVie):
            x = (width - i) * size
            y = 0

            if i < vie_rouge:
                vie = pygame.image.load("img/floor/hearts1.png")
                self.ecran.blit(vie, ((x, y, x + size, y + size)))

            else:
                vie = pygame.image.load("img/floor/hearts2.png")
                self.ecran.blit(vie, ((x, y, x + size, y + size)))

    def affiche_score(self):
        """
        PRE : size doit être de type integer
        POST : Affiche le score en haut a gauche dans le labyrinthe
        """
        police = pygame.font.Font('freesansbold.ttf', 32)
        if self.hero.score < 1000:
            score = police.render("Score: " + str(self.hero.score), True, GREEN)
        elif self.hero.score < 2000:
            score = police.render("Score: " + str(self.hero.score), True, ORANGE)
        elif self.hero.score < 3000:
            score = police.render("Score: " + str(self.hero.score), True, ROUGE)
        elif self.hero.score < 10000:
            score = police.render("Score: " + str(self.hero.score), True, MAUVE)
        self.ecran.blit(score, (10, 10))

    def depl_mobs(self):
        """
        POST : Permet de déplacer les mobs dans le labyrinthe
        """
        self.laby.hero_move(self.hlx, self.hly, self.hx, self.hy)
        [x.deplacement(self.laby) for x in self.mobs]

    def exit(self):
        """
        POST : Permet de fermer l application
        """
        if len(self.item) == 0:
            self.continue_jeu = False

    def set_score(self):
        """
        POST : Permet d'enregistrer le score du personnage entre 2 étage
        """
        self.score = self.hero.score
