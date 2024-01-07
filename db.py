import sqlite3
class DB:
    ''' Класс для работы с таблицами базы данных'''
    def __init__(self):
        ''' Подключение к базе данных'''
        self.connnect = sqlite3.connect("basa.db")
        self.cursor = self.connnect.cursor()

    def check_exist_table(self,table_name):
        ''' Проверка существование таблицы баз данных'''
        self.cursor.execute('''SELECT count(name) FROM sqlite_master WHERE TYPE = 'table' AND name = '{}' '''.format(table_name))
        if self.cursor.fetchone()[0] == 1:
            return True
        return False


    def create(self,table_name):
        if not table_name:
            self.cursor.execute('''CREATE TABLE {}
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER)
            '''.format(table_name))
        else:
            print("Таблица уже создана и существует")
