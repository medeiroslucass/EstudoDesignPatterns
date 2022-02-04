from multiprocessing import connection
import sqlite3


class Singleton(type):

    # se estou herdando de type irei criar metaclasse  
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, *kwargs)
        return cls.__instances[cls]

class Database(metaclass=Singleton):

    connection = None

    def connect(self):
        if self.connection is None:
            print(f'Não temos ainda um conexao... vamos cria-la...')
            self.connection = sqlite3.connect('db.lucas')
            self.cursor = self.connection.cursor()
        return self.cursor


db1 = Database().connect()

db2 = Database().connect()