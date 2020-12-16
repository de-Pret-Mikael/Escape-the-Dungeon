import sqlite3

try:
    connection = sqlite3.connect("escape-the-donjon.db")
    cursor = connection.cursor()
    print("connexion réussi")

    sql = "INSERT INTO Player(nom) VALUE ('George')"

    cursor.execute(sql)
    connection.commit()
    print('insértion correct dans la table player')
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