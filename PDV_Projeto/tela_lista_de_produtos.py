import tkinter as tk
from tkinter import ttk
import sqlite3

# Variável global para armazenar a árvore (Treeview)
tree = None

# Função para buscar todos os produtos do banco de dados
def buscar_produtos():
    # Conecta ao banco de dados e busca todos os produtos na tabela "estoque"
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM estoque''')
    produtos = cursor.fetchall()
    conn.close()
    return produtos

# Cria a janela da interface de listagem de produtos
if __name__ == "__main__":
    root = tk.Tk()
    root.title('Lista de Produtos')

    tree = ttk.Treeview(root, columns=("ID", "Nome", "Descrição", "Categoria", "Preço de Compra", "Preço de Venda", "Quantidade", "Data de Entrada", "Fornecedor", "Notas"), show="headings")

    # Definindo os cabeçalhos das colunas
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Descrição", text="Descrição")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Preço de Compra", text="Preço de Compra")
    tree.heading("Preço de Venda", text="Preço de Venda")
    tree.heading("Quantidade", text="Quantidade")
    tree.heading("Data de Entrada", text="Data de Entrada")
    tree.heading("Fornecedor", text="Fornecedor")
    tree.heading("Notas", text="Notas")

    # Definindo o tamanho máximo de cada coluna
    tree.column("ID", width=50)
    tree.column("Nome", width=150)
    tree.column("Descrição", width=200)
    tree.column("Categoria", width=100)
    tree.column("Preço de Compra", width=100)
    tree.column("Preço de Venda", width=100)
    tree.column("Quantidade", width=80)
    tree.column("Data de Entrada", width=100)
    tree.column("Fornecedor", width=150)
    tree.column("Notas", width=200)

    tree.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # Busca os produtos no banco de dados
    produtos = buscar_produtos()

    # Insere os produtos na tabela (Treeview)
    for produto in produtos:
        tree.insert("", tk.END, values=produto)

    root.mainloop()
