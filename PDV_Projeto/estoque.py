import sqlite3

# Cria uma conexão com o banco de dados
conn = sqlite3.connect('estoque.db')

# Cria a tabela "estoque" com restrições de chave estrangeira para "categoria" e "fornecedor"
conn.execute('''CREATE TABLE estoque (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    descricao TEXT,
    categoria_id INTEGER,
    preco_compra REAL,
    preco_venda REAL,
    quantidade INTEGER,
    data_entrada DATE,
    fornecedor_id INTEGER,
    notas TEXT,
    FOREIGN KEY (categoria_id) REFERENCES categoria(id) ON DELETE CASCADE,
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedor(id) ON DELETE CASCADE
)''')

# Fecha a conexão com o banco de dados
conn.close()
