import sqlite3


class Data:
    def __init__(self, path):
        """
        PRE : path doit être un chemin existant
        POST : initialise l'objet Data
        """
        self.__path = path

    @property
    def path(self):
        return self.__path

    def create_db(self):
        """
        PRE : -
        POST : crée a le fichier db au bonne endroit
        """
        sqlite3.connect(self.path).close()

    def is_db_exist(self):
        """
        PRE : -
        POST : renvoie true si la base de donnée existe, sinon renvoie False
        """
        try:
            sqlite3.connect("file:{}?mode=rw".format(self.path), uri=True).close()
            return True
        except sqlite3.Error:
            return False

    def connect(self):
        """
        PRE : -
        POST : crée les variables connection et cursor
        """
        self.connection = sqlite3.connect("file:{}?mode=rw".format(self.path), uri=True)
        self.cursor = self.connection.cursor()

    def close(self):
        """
        PRE : -
        POST : ferme la liaison avec la base de donnée
        """
        self.cursor.close()
        self.connection.close()

    def __open_sql(self, path):
        """
        PRE : path dois être un chemin existant
        POST : renvoie l intérieur d'un fichier
        """
        try:
            with open(path) as sql_file:
                return sql_file.read()
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

    def use_script(self, path):
        """
        PRE : path doit être un chemin existant vers un fichier sql
        POST : execute le fichier  et enregistre les modification dans la base de donnée
        """
        self.cursor.executescript(self.__open_sql(path))
        self.connection.commit()

    def execute(self, action):
        """
        PRE : action doit être une action sql possible
        POST : execute le sql donner en paramètre et l'enregistre dans la base de donnée
        """
        self.cursor.execute(action)
        self.connection.commit()

    def select_script(self, path):
        """
        PRE : path doit être un chemin existant
        POST : execute le script sql et renvoie les résultat du script sql
        """
        self.use_script(path)
        return self.cursor.fetchall()

    def selectAll(self, nomTable):
        """
        PRE : nomTable doit être un nom de table de la base de donnée
        POST : execute une commande pour avoir tout les informations dans la table demandée et le renvoie résultat
        """
        self.execute("SELECT * FROM {}".format(nomTable))
        return self.cursor.fetchall()



if __name__ == '__main__':
    db = Data("test.db")
    db.connect()
    select = db.selectAll("Mobs")
    db.close()
    dic = {}
    for i in select:
        dic["{}{}".format(i[0],i[1])] = i

