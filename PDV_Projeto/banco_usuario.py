import sqlite3
import bcrypt

# Conectar ao banco de dados "estoque.db" ou criá-lo se não existir
conn = sqlite3.connect("estoque.db")

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar a tabela de usuários
cursor.execute('''CREATE TABLE usuarios (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT,
                  sobrenome TEXT,
                  cpf TEXT,
                  login TEXT,
                  senha TEXT,
                  nivel_acesso TEXT
                )''')

# Função para adicionar um novo usuário ao banco de dados
def adicionar_usuario(nome, sobrenome, cpf, login, senha, nivel_acesso):
    # Criptografar a senha antes de armazená-la no banco de dados
    senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    # Inserir os dados na tabela de usuários
    cursor.execute('''INSERT INTO usuarios (nome, sobrenome, cpf, login, senha, nivel_acesso)
                      VALUES (?, ?, ?, ?, ?, ?)''', (nome, sobrenome, cpf, login, senha_criptografada, nivel_acesso))
    conn.commit()


# Fechar a conexão com o banco de dados
conn.close()
