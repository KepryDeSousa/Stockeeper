import sqlite3

class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
        self.banco = 'Main/Models/config.db/stockeeper.db'

    def salvar(self):
        conn = sqlite3.connect(self.banco)
        cursor = conn.cursor()
        cursor.execute(''' 
            INSERT INTO funcionario (nome, cargo)
            VALUES (?, ?)
        ''', (self.nome, self.cargo))
        conn.commit()
        conn.close()
    
    @staticmethod
    def buscar_todos():
        conn = sqlite3.connect('Main/Models/config.db/stockeeper.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM funcionario')
        funcionarios = cursor.fetchall()
        print(funcionarios)
        conn.close()
    
    @staticmethod
    def limpar_banco():
        conn = sqlite3.connect('Main/Models/config.db/stockeeper.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM funcionario")
        conn.commit()
        conn.close()

if __name__ == '__main__':
    f1 = Funcionario('João', 'Gerente')
    f1.salvar()
    Funcionario.buscar_todos()