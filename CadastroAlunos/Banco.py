import sqlite3

class Banco:

    def __init__(self):
        self.conn = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        cursor = self.conn.cursor()

        cursor.execute("create table if not exists usuarios (idusuario integer primary key autoincrement,nome text,ra text,materia text,media text)")

        self.conn.commit()
        cursor.close()
