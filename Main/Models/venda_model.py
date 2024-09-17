import sqlite3

class Venda:
    def __init__(self, nome: str, quantidade: int, total: float, responsavel: int, produto: int):
        self.nome = nome
        self.quantidade = quantidade
        self.total = total
        self.responsavel = responsavel
        self.produto = produto
        self.banco = 'Main/Models/config.db/stockeeper.db'

    def salvar(self):
        conn = sqlite3.connector(self.banco)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO venda (nome, quantidade, total, responsavel_id, produto_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.nome, self.quantidade, self.total, self.responsavel, self.produto))

        # Atualiza o estoque do produto
        cursor.execute('''
            UPDATE produto
            SET quantidade = quantidade - ?
            WHERE id = ?
        ''', (self.quantidade, self.produto))
        
        conn.commit()

    @staticmethod
    def buscar_todos() -> list:
        """Busca todas as vendas no banco de dados."""
        with sqlite3.connect('Main/Models/config.db/stockeeper.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM venda')
            return cursor.fetchall()


if __name__ == '__name__':
    venda = Venda('Teste', 10, 100.0, 1, 1)
    venda.salvar()
    print(Venda.buscar_todos())