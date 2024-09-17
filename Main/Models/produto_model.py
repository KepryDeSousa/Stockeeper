import sqlite3

class Produto:
    def __init__(self, nome, preco, quantidade, categoria_id='Null'):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria_id = categoria_id
        self.banco = 'Main/Models/config.db/stockeeper.db'

    def salvar(self):
        conn = sqlite3.connect(self.banco)
        cursor = conn.cursor()
        cursor.execute(''' 
            INSERT INTO produto (nome, preco, quantidade, categoria_id)
            VALUES (?, ?, ?, ?)
        ''', (self.nome, self.preco, self.quantidade, self.categoria_id))
        conn.commit()
        conn.close()

    @staticmethod
    def buscar_todos():
        conn = sqlite3.connect('Main/Models/config.db/stockeeper.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM produto')
        produtos = cursor.fetchall()
        conn.close()
        return produtos
    
'''
def limpar_banco():
    conn = sqlite3.connect('Main/Models/config.db/stockeeper.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM produto")
    tabelas = cursor.fetchall()
    conn.commit()
    conn.close()
'''

if __name__ == '__main__':
    p1 = Produto('Coca-Cola', 5.0, 10)
    p1.salvar()
    print(Produto.buscar_todos())
    #limpar_banco()