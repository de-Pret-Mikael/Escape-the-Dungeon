import subprocess
import tkinter
from PIL import Image


class Photo:

    def __init__(self, path, sizetup=(32, 32)):
        """
        initialise l objet photo

        PRE: path doit etre le chemin vers le dossier ou se trouve tout les images que l'on souhait, sizetup doit
        etre un tup de int resemblant a (10,10)

        POST: initialise l objet photo
            path prend comme valeur le paramètre path
            sizetup prend comme valeur le paramètre sizetup
        """
        self.path = path
        self.sizetup = sizetup
        self.build_dict()


    def build_photo(self, name):
        """
        construit l'objet image a partir de son chemin et de son nom

        Pre: nom doit être un string il doit aussi être un nom existant terminant par .png

        POST: renvoie un objet image compose de l image selectionnée

        """
        path = "{}/{}".format(self.path, name)
        img = Image.open(path)
        img = img.resize(self.sizetup, Image.ANTIALIAS)
        return img

    def build_dict(self):
        """
        elle construit le dictionnaire

        PRE : -

        POST : changement de tout l'objet pour qu'il devient un dictionnaire
        """
        lname = self.take_name()
        dic = {}
        for i in lname:
            name = "".join(i.split(".png"))
            dic[name] = self.build_photo(i)
        self.__dict__ = dic

    def take_name(self):
        """
        fonction qui vas chercher tout les nom de différente image dans le dossier selectionné


        PRE : -

        POST : renvoie un liste tout les nom qu il y a dans le dossier
        """

        chemin = "\\".join(self.path.split("/"))
        dir = subprocess.run(["dir", chemin], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             universal_newlines=True)
        find = subprocess.run('find "png"', shell=True, input=dir.stdout, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              universal_newlines=True)
        name = []
        for i in find.stdout.split():
            if "png" in i:
                name.append(i)
        return name


if __name__ == "__main__":
    myapp = tkinter.Tk()
    p = Photo("../../img/dungeon")
    print(p.__dict__)
    # print(p.wallH)
