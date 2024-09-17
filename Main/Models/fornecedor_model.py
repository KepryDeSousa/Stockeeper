import sqlite3

class Fornecedor:
    def __init__(self, nome,telefone,email,categoria_produtos_id='Null'):  
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.banco = 'Main/Models/config.db/stockeeper.db'
        self.categoria_produtos_id = categoria_produtos_id

    def salvar(self):
        conn = sqlite3.connect(self.banco)
        cursor = conn.cursor()
        cursor.execute(''' 
            INSERT INTO fornecedor (nome, telefone, email, categoria_produtos_id)
            VALUES (?, ?, ?, ?)
        ''', (self.nome, self.telefone, self.email,self.categoria_produtos_id))
        conn.commit()
        conn.close()
    
    @staticmethod
    def buscar_todos():
        conn = sqlite3.connect('Main/Models/config.db/stockeeper.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM fornecedor')
        fornecedores = cursor.fetchall()
        print(fornecedores)
        conn.close()
    
    def limpa_banco():
        conn = sqlite3.connect('Main/Models/config.db/stockeeper.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM fornecedor")
        conn.commit()
        conn.close()

if __name__ == '__main__':
    f1 = Fornecedor('Coca-Cola', 123456789, 'teste@email.com')
    f1.salvar()
    #f1.limpa_banco()