# Cria uma conexão com o banco de dados
import sqlite3

conn = sqlite3.connect('estoque.db')

# Cria a tabela "Fornecedor"
conn.execute('''CREATE TABLE IF NOT EXISTS fornecedor
                (fornecedor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome_fantasia TEXT NOT NULL,
                 razao_social TEXT,
                 cnpj TEXT,
                 inscricao_estadual TEXT,
                 inscricao_municipal TEXT,
                 rua TEXT,
                 bairro TEXT,
                 cidade TEXT,
                 estado TEXT,
                 cep TEXT,
                 observacoes TEXT)''')

# Comita as alterações
conn.commit()

# Fecha a conexão com o banco de dados
conn.close()