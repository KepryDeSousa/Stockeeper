CREATE TABLE "produto" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
  "nome" TEXT NOT NULL, -- No postgress é usado Varchar no lugar do text --
  "preco" REAL NOT NULL, -- No postgress é usado Decimal no lugar do real --
  "quantidade" INTEGER NOT NULL,
  "categoria_id" INTEGER NULL,
  FOREIGN KEY ("categoria_id") REFERENCES "categoria" ("id")
);

CREATE TABLE "compra" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
  "nome" TEXT NOT NULL,
  "total" REAL NOT NULL,
  "fornecedor_id" INTEGER NULL,
  "responsavel_id" INTEGER NULL,
  "produto_id" INTEGER NULL,
  data_compra DATE NOT NULL, -- No postgress é usado DATE no lugar do text --
  FOREIGN KEY ("fornecedor_id") REFERENCES "fornecedor" ("id"),
  FOREIGN KEY ("responsavel_id") REFERENCES "funcionario" ("id"),
  FOREIGN KEY ("produto_id") REFERENCES "produto" ("id")
);

CREATE TABLE "categoria" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
  "nome" TEXT NOT NULL
);

CREATE TABLE "funcionario" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
  "nome" TEXT NOT NULL,
  "cargo" TEXT NOT NULL
);

CREATE TABLE "fornecedor" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
  "nome" TEXT NOT NULL,
  "categoria_produtos_id" INTEGER NULL,
  FOREIGN KEY ("categoria_produtos_id") REFERENCES "categoria" ("id")
);

CREATE TABLE "venda" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
  "quantidade" INTEGER NOT NULL,
  "total" REAL NOT NULL,
  "data_venda" TEXT NOT NULL,
  "responsavel_id" INTEGER NULL, 
  "produto_id" INTEGER NULL,
  FOREIGN KEY ("responsavel_id") REFERENCES "funcionario" ("id"),
  FOREIGN KEY ("produto_id") REFERENCES "produto" ("id")
);
