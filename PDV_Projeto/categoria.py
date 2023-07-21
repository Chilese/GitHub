import sqlite3

# Cria uma conexão com o banco de dados
conn = sqlite3.connect('estoque.db')

# Cria a tabela "Categoria"
conn.execute('''CREATE TABLE IF NOT EXISTS categoria
                (categoria_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 categoria TEXT NOT NULL)''')

# Comita as alterações
conn.commit()

# Fecha a conexão com o banco de dados
conn.close()