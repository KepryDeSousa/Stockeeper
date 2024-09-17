import sqlite3

def criar_tabelas():

    conn = sqlite3.connect("Main/Models/config.db/stockeeper.db")
    cursor = conn.cursor()
    
   
    cursor.execute("PRAGMA foreign_keys = ON;") # Habilitar chaves estrangeiras
    

    tabelas_sql = '''
    CREATE TABLE IF NOT EXISTS "categoria" (
      "id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
      "nome" TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS "produto" (
      "id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
      "nome" TEXT NOT NULL, -- No postgres seria varchar(255)--
      "preco" REAL NOT NULL,
      "quantidade" INTEGER NOT NULL,
      "categoria_id" INTEGER NULL,
      FOREIGN KEY ("categoria_id") REFERENCES "categoria" ("id")
    );

    CREATE TABLE IF NOT EXISTS "funcionario" (
      "id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
      "nome" TEXT NOT NULL,
      "cargo" TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS "fornecedor" (
      "id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
      "nome" TEXT NOT NULL,
      "categoria_produtos_id" INTEGER NULL,
      "telefone" INTEGER NULL,
      "email" TEXT NULL,
      FOREIGN KEY ("categoria_produtos_id") REFERENCES "categoria" ("id")
    );

    CREATE TABLE IF NOT EXISTS "compra" (
      "id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
      "nome" TEXT NOT NULL,
      "total" REAL NOT NULL,
      "fornecedor_id" INTEGER NULL,
      "responsavel_id" INTEGER NULL,
      "produto_id" INTEGER,
      "data_compra" TEXT NOT NULL,
      FOREIGN KEY ("fornecedor_id") REFERENCES "fornecedor" ("id"),
      FOREIGN KEY ("responsavel_id") REFERENCES "funcionario" ("id"),
      FOREIGN KEY ("produto_id") REFERENCES "produto" ("id")
    );

    CREATE TABLE IF NOT EXISTS "venda" (
      "id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
      "quantidade" INTEGER NOT NULL,
      "total" REAL NOT NULL,
      "data_venda" TEXT NOT NULL,
      "responsavel_id" INTEGER,
      "produto_id" INTEGER,
      FOREIGN KEY ("responsavel_id") REFERENCES "funcionario" ("id"),
      FOREIGN KEY ("produto_id") REFERENCES "produto" ("id")
    );
    '''
    
    # Executar a criação das tabelas
    cursor.executescript(tabelas_sql)

    # Confirmar mudanças
    conn.commit()
    conn.close()

# Executar a função
criar_tabelas()
