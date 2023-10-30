import sqlite3

# Conecta ao banco de dados ou cria um novo se não existir
conn = sqlite3.connect("estoque.db")
cursor = conn.cursor()

# Cria a tabela "vendas"
cursor.execute('''CREATE TABLE vendas (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  cpf_cliente TEXT,
                  forma_pagamento TEXT,
                  total_compra REAL,
                  data_hora_venda TEXT)''')

# Commita as alterações e fecha a conexão com o banco de dados
conn.commit()
conn.close()
