import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import subprocess
import os

class InterfaceGestaoUsuarios:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Usuários")

        # Criar a tabela para exibir os usuários
        self.tree = ttk.Treeview(root, columns=("ID", "Nome", "Sobrenome", "CPF", "Login", "Nível de Acesso"))
        self.tree.heading("#0", text="", anchor="w")
        self.tree.heading("#1", text="ID", anchor="w")
        self.tree.heading("#2", text="Nome", anchor="w")
        self.tree.heading("#3", text="Sobrenome", anchor="w")
        self.tree.heading("#4", text="CPF", anchor="w")
        self.tree.heading("#5", text="Login", anchor="w")
        self.tree.heading("#6", text="Nível de Acesso", anchor="w")
        self.tree.pack(padx=10, pady=10)

        # Adicionar evento de duplo clique
        self.tree.bind("<Double-1>", self.editar_usuario)

        # Adicionar botão "Criar Usuário"
        tk.Button(root, text="Criar Usuário", command=self.criar_usuario).pack(pady=10)

        # Preencher a tabela com os usuários do banco de dados
        self.carregar_usuarios()
    
    def criar_usuario(self):
        # Executar o código administrativa_cadastro_usuario.py
        script_path = os.path.join(os.path.dirname(__file__), "administrativa_cadastro_usuario.py")
        subprocess.Popen(["python", script_path])

    def carregar_usuarios(self):
        # Conectar ao banco de dados
        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()

        # Selecionar todos os usuários
        cursor.execute("SELECT id, nome, sobrenome, cpf, login, nivel_acesso FROM usuarios")
        usuarios = cursor.fetchall()

        # Limpar a tabela
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Adicionar os usuários à tabela
        for usuario in usuarios:
            self.tree.insert("", "end", values=usuario)

        # Fechar a conexão
        conn.close()

    def excluir_usuario(self):
        # Obter o ID do usuário selecionado
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Selecione um usuário para excluir.")
            return

        id_usuario = self.tree.item(selected_item, "values")[0]

        # Confirmar a exclusão
        confirmacao = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este usuário?")
        if not confirmacao:
            return

        # Conectar ao banco de dados
        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()

        # Excluir o usuário do banco de dados
        cursor.execute("DELETE FROM usuarios WHERE id=?", (id_usuario,))

        # Commit e fechar a conexão
        conn.commit()
        conn.close()

        # Atualizar a tabela
        self.carregar_usuarios()

    def editar_usuario(self, event=None):
        # Obter o ID do usuário selecionado
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Selecione um usuário para editar.")
            return

        id_usuario = self.tree.item(selected_item, "values")[0]

        # Conectar ao banco de dados
        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()

        # Selecionar os detalhes do usuário
        cursor.execute("SELECT id, nome, sobrenome, cpf, login, nivel_acesso FROM usuarios WHERE id=?", (id_usuario,))
        usuario_detalhes = cursor.fetchone()

        # Fechar a conexão
        conn.close()

        # Criar a janela de edição
        janela_edicao = tk.Toplevel(self.root)
        janela_edicao.title("Editar Usuário")

        # Layout da janela de edição
        tk.Label(janela_edicao, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(janela_edicao, text=usuario_detalhes[0]).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(janela_edicao, text="Nome:").grid(row=1, column=0, padx=10, pady=10)
        nome_var = tk.StringVar(value=usuario_detalhes[1])
        tk.Entry(janela_edicao, textvariable=nome_var).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(janela_edicao, text="Sobrenome:").grid(row=2, column=0, padx=10, pady=10)
        sobrenome_var = tk.StringVar(value=usuario_detalhes[2])
        tk.Entry(janela_edicao, textvariable=sobrenome_var).grid(row=2, column=1, padx=10, pady=10)

        tk.Label(janela_edicao, text="CPF:").grid(row=3, column=0, padx=10, pady=10)
        cpf_var = tk.StringVar(value=usuario_detalhes[3])
        tk.Entry(janela_edicao, textvariable=cpf_var).grid(row=3, column=1, padx=10, pady=10)

        tk.Label(janela_edicao, text="Login:").grid(row=4, column=0, padx=10, pady=10)
        login_var = tk.StringVar(value=usuario_detalhes[4])
        tk.Entry(janela_edicao, textvariable=login_var).grid(row=4, column=1, padx=10, pady=10)

        tk.Label(janela_edicao, text="Nível de Acesso:").grid(row=5, column=0, padx=10, pady=10)
        nivel_acesso_var = tk.StringVar(value=usuario_detalhes[5])
        tk.Entry(janela_edicao, textvariable=nivel_acesso_var).grid(row=5, column=1, padx=10, pady=10)

        # Função para salvar as alterações
        def salvar_edicao():
            # Conectar ao banco de dados
            conn = sqlite3.connect("estoque.db")
            cursor = conn.cursor()

            # Atualizar os dados do usuário no banco de dados
            cursor.execute("UPDATE usuarios SET nome=?, sobrenome=?, cpf=?, login=?, nivel_acesso=? WHERE id=?",
                           (nome_var.get(), sobrenome_var.get(), cpf_var.get(), login_var.get(), nivel_acesso_var.get(), id_usuario))

            # Commit e fechar a conexão
            conn.commit()
            conn.close()

            # Atualizar a tabela
            self.carregar_usuarios()

            # Fechar a janela de edição
            janela_edicao.destroy()

        # Botão para salvar as alterações
        tk.Button(janela_edicao, text="Salvar", command=salvar_edicao).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Botão "Excluir" dentro da tela de edição
        tk.Button(janela_edicao, text="Excluir", command=self.excluir_usuario).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Criar a janela principal
root = tk.Tk()
interface_gestao_usuarios = InterfaceGestaoUsuarios(root)
root.mainloop()
