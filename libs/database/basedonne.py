import sqlite3


class Data:
    def __init__(self, path):
        self.__path = path

    @property
    def path(self):
        return self.__path

    def is_db_exist(self):
        try:
            sqlite3.connect("file:{}?mode=rw".format(self.path), uri=True).close()
            return True
        except sqlite3.Error:
            return False

    def connect(self):
        self.connection = sqlite3.connect("file:{}?mode=rw".format(self.path), uri=True)
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def __open_sql(self, path):
        try:
            with open(path) as sql_file:
                return sql_file.read()
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

    def use_script(self, path):
        self.cursor.executescript(self.__open_sql(path))
        self.connection.commit()

    def execute(self, action):
        self.cursor.execute(action)
        self.connection.commit()

    def insert(self, table, nameRows, value):
        value = ["'" + i + "'" for i in value]
        value = ", ".join(value)
        action = "INSERT INTO {}({}) VALUES ({})".format(table, nameRows, value)
        self.execute(action)

    def select(self, path):
        self.use_script(path)
        return self.cursor.fetchall()


def create_db(path):
    sqlite3.connect(path).close()
    newDb = Data(path)
    newDb.connect()
    newDb.use_script("../../DATA/createTable.sql")
    newDb.use_script("../../DATA/insertData.sql")
    newDb.close()



if __name__ == '__main__':
    create_db("test.db")
