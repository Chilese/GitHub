import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

# Função para inserir um novo produto no estoque
def inserir_produto():
    nome = entry_nome.get()
    descricao = entry_descricao.get()
    categoria_id = int(entry_categoria_id.get())  # Supondo que a categoria_id seja um campo com valores inteiros
    preco_compra = float(entry_preco_compra.get())
    preco_venda = float(entry_preco_venda.get())
    quantidade = int(entry_quantidade.get())
    data_entrada = entry_data_entrada.get()
    fornecedor_id = int(entry_fornecedor_id.get())  # Supondo que o fornecedor_id seja um campo com valores inteiros
    notas = entry_notas.get()

    # Conecta ao banco de dados e insere os dados na tabela "estoque"
    db_path = os.path.abspath("estoque.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO estoque (nome, descricao, categoria_id, preco_compra, preco_venda, quantidade, data_entrada, fornecedor_id, notas)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (nome, descricao, categoria_id, preco_compra, preco_venda, quantidade, data_entrada, fornecedor_id, notas))
    conn.commit()
    conn.close()

    messagebox.showinfo('Sucesso', 'Produto inserido com sucesso!')

# Função para editar um produto pelo nome
def editar_produto():
    nome_produto = entry_nome.get()

    # Conecta ao banco de dados e busca os dados do produto pelo nome
    db_path = os.path.abspath("estoque.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM estoque WHERE nome=?''', (nome_produto,))
    produto = cursor.fetchone()
    conn.close()

    if not produto:
        messagebox.showwarning('Produto não encontrado', 'O produto com o nome informado não foi encontrado.')
        return

    # Preenche os campos de entrada com os dados existentes do produto
    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, produto[1])

    entry_descricao.delete(0, tk.END)
    entry_descricao.insert(0, produto[2])

    entry_categoria_id.delete(0, tk.END)
    entry_categoria_id.insert(0, produto[3])

    entry_preco_compra.delete(0, tk.END)
    entry_preco_compra.insert(0, produto[4])

    entry_preco_venda.delete(0, tk.END)
    entry_preco_venda.insert(0, produto[5])

    entry_quantidade.delete(0, tk.END)
    entry_quantidade.insert(0, produto[6])

    entry_data_entrada.delete(0, tk.END)
    entry_data_entrada.insert(0, produto[7])

    entry_fornecedor_id.delete(0, tk.END)
    entry_fornecedor_id.insert(0, produto[8])

    entry_notas.delete(0, tk.END)
    entry_notas.insert(0, produto[9])

# Função para excluir um produto pelo nome
def excluir_produto():
    nome_produto = entry_nome.get()

    # Conecta ao banco de dados e exclui o produto pelo nome
    db_path = os.path.abspath("estoque.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM estoque WHERE nome=?''', (nome_produto,))
    conn.commit()
    conn.close()

    messagebox.showinfo('Produto excluído', 'O produto foi excluído com sucesso!')

    # Limpa os campos de entrada após a exclusão
    entry_nome.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)
    entry_categoria_id.delete(0, tk.END)
    entry_preco_compra.delete(0, tk.END)
    entry_preco_venda.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_data_entrada.delete(0, tk.END)
    entry_fornecedor_id.delete(0, tk.END)
    entry_notas.delete(0, tk.END)

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

label_categoria_id = tk.Label(root, text='Categoria ID:')
label_categoria_id.grid(row=2, column=0)
entry_categoria_id = tk.Entry(root)
entry_categoria_id.grid(row=2, column=1)

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

label_fornecedor_id = tk.Label(root, text='Fornecedor ID:')
label_fornecedor_id.grid(row=7, column=0)
entry_fornecedor_id = tk.Entry(root)
entry_fornecedor_id.grid(row=7, column=1)

label_notas = tk.Label(root, text='Notas:')
label_notas.grid(row=8, column=0)
entry_notas = tk.Entry(root)
entry_notas.grid(row=8, column=1)

# Botões para executar as operações
btn_inserir = tk.Button(root, text='Inserir', command=inserir_produto)
btn_inserir.grid(row=9, column=0)

btn_editar = tk.Button(root, text='Editar', command=editar_produto)
btn_editar.grid(row=9, column=1)

btn_excluir = tk.Button(root, text='Excluir', command=excluir_produto)
btn_excluir.grid(row=9, column=2)

# Inicia a execução da interface
root.mainloop()