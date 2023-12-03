import sqlite3

# Conecta ao banco de dados ou cria um novo se não existir
conn = sqlite3.connect("estoque.db")
cursor = conn.cursor()

# Cria a tabela "itens_venda"
cursor.execute('''CREATE TABLE itens_venda (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  venda_id INTEGER,
                  produto_nome TEXT,
                  quantidade INTEGER,
                  FOREIGN KEY (venda_id) REFERENCES vendas (id))''')

# Commita as alterações e fecha a conexão com o banco de dados
conn.commit()
conn.close()
