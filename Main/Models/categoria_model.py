import sqlite3

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.banco = 'Main/Models/config.db/stockeeper.db'

    def salvar(self):
        conn = sqlite3.connect(self.banco)
        cursor = conn.cursor()
        cursor.execute(''' 
            INSERT INTO categoria (nome)
            VALUES (?)
        ''', (self.nome,))
        conn.commit()
        conn.close()


    
    @staticmethod
    def buscar_todos():
        conn = sqlite3.connect('Main/Models/config.db/stockeeper.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM categoria')
        categorias = cursor.fetchall()
        print(categorias)
        conn.close()
    
    @staticmethod
    def limpar_banco():
        conn = sqlite3.connect('Main/Models/config.db/stockeeper.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categoria")
        conn.commit()
        conn.close()


if __name__ == '__main__':
    Categoria('Bebidas Quentes').salvar()
    #Categoria.limpar_banco()
