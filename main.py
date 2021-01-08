from libs.labyrinthe import *
from libs.hero import *
import os

if __name__ == "__main__":
    lab = Labyrinthe(2, 2)
    png = Hero()
    png.set_posi(**lab.start)
    lab.show()
    while not png.fin:
        png.choix_deplacement(lab)
        os.system("cls")
        if png.fin:
            print('Vous avez réussi à sortir, bien jouer')
        heroPos = {"lastx": png.lastx, "lasty": png.lasty, "newx": png.x, "newy": png.y}
        lab.hero_move(**heroPos)
        lab.show()
