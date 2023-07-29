import tkinter as tk
import sqlite3

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
def criar_lista_produtos():
    root = tk.Toplevel()
    root.title('Lista de Produtos')

    # Cria uma lista para exibir os produtos
    lista = tk.Listbox(root, width=80)
    lista.grid(row=0, column=0, columnspan=3)

    # Busca os produtos no banco de dados
    produtos = buscar_produtos()

    # Insere os produtos na lista
    for produto in produtos:
        lista.insert(tk.END, produto[0])  # Aqui, estamos usando o id do produto como identificador

    # Botão para abrir a janela de cadastro de produto
    btn_cadastrar_produto = tk.Button(root, text='Cadastro de Produto', command=abrir_interface_cadastro)
    btn_cadastrar_produto.grid(row=1, column=0, columnspan=3)

    root.mainloop()

# Função para abrir a janela de cadastro de produtos (interface.py)
def abrir_interface_cadastro():
    import interface

# Chama a função para criar a interface de listagem de produtos
criar_lista_produtos()