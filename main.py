from libs.labyrinthe import *
from libs.hero import *
import os

if __name__ == "__main__":
    l = Labyrinthe(2, 2)
    png = hero()
    png.setPosi(**l.start)
    l.show()
    while not png.fin:
        png.choix_deplacement(l)
        os.system("cls")
        if png.fin:
            print('Vous avez réussi à sortir, bien jouer')
        heroPos = {"lastx": png.lastx, "lasty": png.lasty, "newx": png.x, "newy": png.y}
        l.hero_move(**heroPos)
        l.show()
