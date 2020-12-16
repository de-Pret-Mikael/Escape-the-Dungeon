import sqlite3


class Data:
    def __init__(self, path):
        self.path = path

    def connect(self):
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

    def execute(self, action):
        self.cursor.execute(action)

    def insert(self, table, nameRows, value):
        value = ["'" + i + "'" for i in value]
        value = ", ".join(value)
        action = "INSERT INTO {}({}) VALUES ({})".format(table, nameRows, value)
        self.execute(action)


if __name__ == '__main__':
    db = Data("escape-the-donjon.db")
    db.connect()
    db.execute("INSERT INTO Player(nom) VALUES ('test')")
    db.insert("Player", "nom", ["test123"])
    db.cursor.close()
    db.connection.close()
