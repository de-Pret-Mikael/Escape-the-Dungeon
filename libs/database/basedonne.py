import sqlite3


class Data:
    def __init__(self, path):
        self.path = path
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()

    def open_sql(self, path):
        try:
            with open(path) as sql_file:
                return sql_file
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

    def use_script(self, path):
        self.cursor.executescript(self.open_sql(path))


try:
    connection = sqlite3.connect("escape-the-donjon.db")
    cursor = connection.cursor()
    print("connexion réussi")

    sql = "INSERT INTO Player(nom) VALUE ('George')"

    cursor.execute(sql)
    connection.commit()
    print('insertion correct dans la table player')
    cursor.close()
    connection.close()
    print('connection à SQL terminé')

except sqlite3.Error as error:
    print("Erreur lors de ajout name")

"""import sqlite3
from libs.affichage import *

gui = Gui()
try:
    connection = sqlite3.connect("escape-the-donjon.db")
    cursor = connection.cursor()
    print("connexion réussi")

    sql = "INSERT INTO Player nom VALUE (?)"

    value = gui.set_name

    cursor.execute(sql)
    connection.commit()
    print('insértion correct dans la table player')
    cursor.close()
    connection.close()
    print('connection à SQL terminé')

except sqlite3.Error as error:
    print("Erreur lors de ajout name")
"""
