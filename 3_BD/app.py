import sqlite3

conexao = sqlite3.connect('banco.db')
#cursor init 
cursor = conexao.cursor()

cursor.execute ('''
                CREATE TABLE IF NOT EXISTS authots (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    born_date TEXT
)''')
