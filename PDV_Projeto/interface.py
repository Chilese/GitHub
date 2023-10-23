import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import os

def obter_nomes_fornecedores():
    # Código para obter nomes de fornecedores do banco de dados
    pass

def obter_nomes_categorias():
<<<<<<< HEAD
    # Código para obter nomes de categorias do banco de dados
    pass
=======
    # Função para obter os nomes das categorias do banco de dados
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT categoria FROM categoria''')
    categorias = cursor.fetchall()
    conn.close()
    return [categoria[0] for categoria in categorias]

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
combo_categoria_id = ttk.Combobox(root, values=obter_nomes_categorias())  # Configuração do combobox
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
combo_fornecedor = ttk.Combobox(root, values=obter_nomes_fornecedores())  # Configuração da combobox
combo_fornecedor.grid(row=7, column=1)

label_notas = tk.Label(root, text='Notas:')
label_notas.grid(row=8, column=0)
entry_notas = tk.Entry(root)
entry_notas.grid(row=8, column=1)


# Função para inserir um novo produto no estoque
def inserir_produto():
    nome = entry_nome.get()
    descricao = entry_descricao.get()
    categoria_id = combo_categoria_id.get()
    preco_compra = float(entry_preco_compra.get())
    preco_venda = float(entry_preco_venda.get())
    quantidade = int(entry_quantidade.get())
    data_entrada = entry_data_entrada.get()
    fornecedor = combo_fornecedor.get()  # Obtém o fornecedor selecionado
    notas = entry_notas.get()

    # Conecta ao banco de dados e busca o fornecedor_id pelo nome do fornecedor
    db_path = os.path.abspath("estoque.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''SELECT fornecedor_id FROM fornecedor WHERE nome_fantasia=?''', (fornecedor,))
    result = cursor.fetchone()
    conn.close()

    if result:
        fornecedor_id = result[0]
    else:
        # Fornecedor não encontrado, trate isso de acordo com suas necessidades
        fornecedor_id = None

    # Conecta ao banco de dados e insere os dados na tabela "estoque"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO estoque (nome, descricao, categoria_id, preco_compra, preco_venda, quantidade, data_entrada, fornecedor_id, notas)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (nome, descricao, categoria_id, preco_compra, preco_venda, quantidade, data_entrada, fornecedor_id, notas))
    conn.commit()
    conn.close()

    messagebox.showinfo('Sucesso', 'Produto inserido com sucesso!')


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

    combo_categoria = ttk.Combobox(root, values=obter_nomes_categorias())
    combo_categoria.set(produto[3])

    entry_preco_compra.delete(0, tk.END)
    entry_preco_compra.insert(0, produto[4])

    entry_preco_venda.delete(0, tk.END)
    entry_preco_venda.insert(0, produto[5])

    entry_quantidade.delete(0, tk.END)
    entry_quantidade.insert(0, produto[6])

    entry_data_entrada.delete(0, tk.END)
    entry_data_entrada.insert(0, produto[7])

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
    entry_preco_compra.delete(0, tk.END)
    entry_preco_venda.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_data_entrada.delete(0, tk.END)
    entry_notas.delete(0, tk.END)
>>>>>>> 7fdbd8ee8adb00d188cbf1939d9af063129a5d61

# Cria os campos de entrada e rótulos para cada campo da tabela
label_nome = tk.Label(root, text='Nome:')
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

label_descricao = tk.Label(root, text='Descrição:')
label_descricao.grid(row=1, column=0)
entry_descricao = tk.Entry(root)
entry_descricao.grid(row=1, column=1)

<<<<<<< HEAD
label_categoria_id = tk.Label(root, text='Categoria:')
label_categoria_id.grid(row=2, column=0)
combo_categoria_id = ttk.Combobox(root, values=obter_nomes_categorias(), width=20)  # Defina a largura aqui
combo_categoria_id.grid(row=2, column=1)

=======
>>>>>>> 7fdbd8ee8adb00d188cbf1939d9af063129a5d61
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

<<<<<<< HEAD
label_fornecedor = tk.Label(root, text='Fornecedor:')
label_fornecedor.grid(row=7, column=0)
combo_fornecedor = ttk.Combobox(root, values=obter_nomes_fornecedores(), width=20)  # Defina a largura aqui
combo_fornecedor.grid(row=7, column=1)

=======
>>>>>>> 7fdbd8ee8adb00d188cbf1939d9af063129a5d61
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
