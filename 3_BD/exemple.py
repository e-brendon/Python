import sqlite3

def inserir_autor(nome):
    with sqlite3.connect("my_db.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS authors (id INTEGER PRIMARY KEY, name TEXT)")
        cursor.execute("INSERT INTO authors (name)  VALUES (?)", (nome, ))

def listar_autores():
    with sqlite3.connect("my_db.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM authors LIMIT 2")
        for linha in cursor.fetchall():
            print(linha)
        
inserir_autor("Meg a dog")
listar_autores()
