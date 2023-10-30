import tkinter as tk
from tkinter import ttk
import sqlite3
import bcrypt
from tkinter import messagebox

class InterfaceAdministrativa:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface Administrativa")

        # Variáveis
        self.nome = tk.StringVar()
        self.sobrenome = tk.StringVar()
        self.cpf = tk.StringVar()
        self.senha = tk.StringVar()
        self.niveis_acesso = ["Administrativo", "Vendedor", "Estoquista"]
        self.nivel_acesso_selecionado = tk.StringVar()

        # Layout
        label_nome = tk.Label(root, text="Nome:")
        label_nome.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        entry_nome = tk.Entry(root, textvariable=self.nome)
        entry_nome.grid(row=0, column=1, padx=10, pady=10)

        label_sobrenome = tk.Label(root, text="Sobrenome:")
        label_sobrenome.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        entry_sobrenome = tk.Entry(root, textvariable=self.sobrenome)
        entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

        label_cpf = tk.Label(root, text="CPF:")
        label_cpf.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        entry_cpf = tk.Entry(root, textvariable=self.cpf)
        entry_cpf.grid(row=2, column=1, padx=10, pady=10)

        label_nivel_acesso = tk.Label(root, text="Nível de Acesso:")
        label_nivel_acesso.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        combo_nivel_acesso = ttk.Combobox(root, textvariable=self.nivel_acesso_selecionado, values=self.niveis_acesso)
        combo_nivel_acesso.grid(row=3, column=1, padx=10, pady=10)

        label_login = tk.Label(root, text="Login:")
        label_login.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.login_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.login_label.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        label_senha = tk.Label(root, text="Senha:")
        label_senha.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        entry_senha = tk.Entry(root, textvariable=self.senha, show='*')
        entry_senha.grid(row=5, column=1, padx=10, pady=10)

        botao_criar_usuario = tk.Button(root, text="Criar Usuário", command=self.criar_usuario)
        botao_criar_usuario.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Adicione a função atualizar_login à seleção no combobox
        combo_nivel_acesso.bind("<<ComboboxSelected>>", self.atualizar_login)

    def criar_usuario(self):
        nome = self.nome.get()
        sobrenome = self.sobrenome.get()
        cpf = self.cpf.get()
        nivel_acesso = self.nivel_acesso_selecionado.get()
        senha = self.senha.get()

        # Gerar login (nome@sobrenome)
        login = f"{nome.lower()}_{sobrenome.lower()}"

        # Hash da senha usando bcrypt
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Conectar ao banco de dados
        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()

        # Inserir novo usuário na tabela
        cursor.execute("INSERT INTO usuarios (nome, sobrenome, cpf, login, senha, nivel_acesso) VALUES (?, ?, ?, ?, ?, ?)",
                       (nome, sobrenome, cpf, login, senha_hash, nivel_acesso))

        # Commit e fechar a conexão
        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Usuário criado com sucesso.")
        self.limpar_campos()

    def atualizar_login(self, event):
        # Obtenha o nome e sobrenome dos campos correspondentes
        nome = self.nome.get().lower()
        sobrenome = self.sobrenome.get().lower()

        # Obtenha o nível de acesso selecionado
        nivel_acesso = self.nivel_acesso_selecionado.get().lower()

        # Gere o login (nome@sobrenome) apenas se nome, sobrenome e nível de acesso não estiverem vazios
        if nome and sobrenome and nivel_acesso:
            login = f"{nome}_{sobrenome}"
            self.login_label.config(text=login)  # Atualize o texto do Label com o login

    def limpar_campos(self):
        self.nome.set("")
        self.sobrenome.set("")
        self.cpf.set("")
        self.nivel_acesso_selecionado.set("")
        self.senha.set("")
        self.login_label.config(text="")

# Criar a janela principal
root = tk.Tk()
interface_administrativa = InterfaceAdministrativa(root)
root.mainloop()
