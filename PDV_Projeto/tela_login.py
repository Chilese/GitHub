import tkinter as tk
import sqlite3
import bcrypt
from tkinter import messagebox

class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        self.label_usuario = tk.Label(root, text="Nome de Usuário:")
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()

        self.label_senha = tk.Label(root, text="Senha:")
        self.label_senha.pack()
        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.pack()

        self.botao_login = tk.Button(root, text="Login", command=self.verificar_credenciais)
        self.botao_login.pack()

    def verificar_credenciais(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        # Conectar ao banco de dados
        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()

        # Buscar as credenciais do usuário no banco de dados
        cursor.execute("SELECT senha, nivel_acesso FROM usuarios WHERE login = ?", (usuario,))
        resultado = cursor.fetchone()

        # Fechar a conexão com o banco de dados
        conn.close()

        # Verificar se as credenciais são válidas
        if resultado:
            senha_hash = resultado[0]
            nivel_acesso = resultado[1]

            # Verificar a senha usando bcrypt
            if bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8')):
                messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario}! Nível de acesso: {nivel_acesso}")
                # Implementar a lógica de controle de acesso aqui
            else:
                messagebox.showerror("Erro", "Credenciais inválidas.")
        else:
            messagebox.showerror("Erro", "Credenciais inválidas.")

# Criar a janela principal
root = tk.Tk()
tela_login = TelaLogin(root)
root.mainloop()
