import sqlite3

import datetime

class Compra():
    def __init__(self,nome,total,fornecedor,responsavel,produto):
        self.nome = nome
        self.fornecedor = fornecedor
        self.responsavel = responsavel
        self.produto = produto
        self.data_compra = datetime.datetime.now()
        self.banco = 'Main/Models/config.db/stockeeper.db'
        self.total = total

    def salvar(self):
        conn = sqlite3.connect(self.banco)
        cursor = conn.cursor()
        cursor.execute(''' 
            INSERT INTO compra (nome, total,fornecedor_id, responsavel_id, produto_id, data_compra)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.nome, self.total,self.fornecedor, self.responsavel, self.produto, self.data_compra))
        conn.commit()
        import sqlite3

class Venda:
    def __init__(self, nome: str, quantidade: int, total: float, responsavel: int, produto: int):
        self.nome = nome
        self.quantidade = quantidade
        self.total = total
        self.responsavel = responsavel
        self.produto = produto
        self.banco = 'Main/Models/config.db/stockeeper.db'

    def salvar(self) -> None:
        """Salva uma nova venda no banco de dados e atualiza o estoque do produto."""
        with sqlite3.connect(self.banco) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO venda (nome, quantidade, total, responsavel_id, produto_id)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.nome, self.quantidade, self.total, self.responsavel, self.produto))

            # Atualiza o estoque do produto
            cursor.execute('''
                UPDATE produto
                SET quantidade = quantidade + ?
                WHERE id = ?
            ''', (self.quantidade, self.produto))
            
            conn.commit()


    @staticmethod
    def buscar_todos():
        conn = sqlite3.connect('Main/Models/config.db/stockeeper.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM compra')
        compras = cursor.fetchall()
        conn.close()
        return compras
    
    @staticmethod
    def limpa_dados():
        conn = sqlite3.connect('Main/Models/config.db/stockeeper.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM compra")
        conn.commit()
        conn.close()   
    
if __name__ == '__main__':
    c1 = Compra('Compra de produtos',54.2, 1, 1, 1)
    c1.salvar()
    print(Compra.buscar_todos())
    #Compra.limpa_dados()
    hora_e_dia_atual = datetime.datetime.now()
    print(hora_e_dia_atual)