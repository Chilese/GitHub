import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import os

def obter_nomes_fornecedores():
    # Código para obter nomes de fornecedores do banco de dados
    pass

def obter_nomes_categorias():
    # Código para obter nomes de categorias do banco de dados
    pass

# Cria a janela da interface
root = tk.Tk()
root.title('Cadastro de Produtos')

# Cria os campos de entrada e rótulos para cada campo da tabela
label_nome = tk.Label(root, text='Nome:')
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

label_descricao = tk.Label(root, text='Descrição:')
label_descricao.grid(row=1, column=0)
entry_descricao = tk.Entry(root)
entry_descricao.grid(row=1, column=1)

label_categoria_id = tk.Label(root, text='Categoria:')
label_categoria_id.grid(row=2, column=0)
combo_categoria_id = ttk.Combobox(root, values=obter_nomes_categorias(), width=20)  # Defina a largura aqui
combo_categoria_id.grid(row=2, column=1)

label_preco_compra = tk.Label(root, text='Preço de Compra:')
label_preco_compra.grid(row=3, column=0)
entry_preco_compra = tk.Entry(root)
entry_preco_compra.grid(row=3, column=1)

label_preco_venda = tk.Label(root, text='Preço de Venda:')
label_preco_venda.grid(row=4, column=0)
entry_preco_venda = tk.Entry(root)
entry_preco_venda.grid(row=4, column=1)

label_quantidade = tk.Label(root, text='Quantidade:')
label_quantidade.grid(row=5, column=0)
entry_quantidade = tk.Entry(root)
entry_quantidade.grid(row=5, column=1)

label_data_entrada = tk.Label(root, text='Data de Entrada:')
label_data_entrada.grid(row=6, column=0)
entry_data_entrada = tk.Entry(root)
entry_data_entrada.grid(row=6, column=1)

label_fornecedor = tk.Label(root, text='Fornecedor:')
label_fornecedor.grid(row=7, column=0)
combo_fornecedor = ttk.Combobox(root, values=obter_nomes_fornecedores(), width=20)  # Defina a largura aqui
combo_fornecedor.grid(row=7, column=1)

label_notas = tk.Label(root, text='Notas:')
label_notas.grid(row=8, column=0)
entry_notas = tk.Entry(root)
entry_notas.grid(row=8, column=1)

# Cria uma célula vazia na coluna 1 e linha 9 para centralizar o botão Inserir
tk.Label(root, text='').grid(row=9, column=1)

# Função para inserir um novo produto no estoque
def inserir_produto():
    # Código para inserir um novo produto no banco de dados
    pass

# Botão para executar a operação de inserção, centralizado na parte inferior
btn_inserir = tk.Button(root, text='Inserir', command=inserir_produto)
btn_inserir.grid(row=9, column=0, columnspan=2)  # Utiliza columnspan para ocupar duas colunas

# Inicia a execução da interface
root.mainloop()
