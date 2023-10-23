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

# Função para exibir detalhes do produto em uma janela pop-up
def exibir_detalhes_produto(event):
    # Obter o ID do item selecionado
    item_id = tree.focus()

    # Obter os valores (colunas) do item selecionado
    valores = tree.item(item_id, 'values')

    # Criar a janela pop-up para exibir os detalhes do produto
    popup = tk.Toplevel(root)
    popup.title('Detalhes do Produto')

    # Criar rótulos e exibir os detalhes do produto
    for i, coluna in enumerate(tree["columns"]):
        label = tk.Label(popup, text=f"{tree.heading(coluna)['text']}: {valores[i]}")
        label.pack()

# Função para abrir a janela de cadastro de fornecedor
def abrir_cadastro_fornecedor():
    popup = tk.Toplevel(root)
    popup.title('Cadastro de Fornecedor')

    # Rótulos e campos para cadastrar o fornecedor
    label_nome_fantasia = tk.Label(popup, text='Nome Fantasia:')
    label_nome_fantasia.pack()
    entry_nome_fantasia = tk.Entry(popup)
    entry_nome_fantasia.pack()

    label_razao_social = tk.Label(popup, text='Razão Social:')
    label_razao_social.pack()
    entry_razao_social = tk.Entry(popup)
    entry_razao_social.pack()

    label_cnpj = tk.Label(popup, text='CNPJ:')
    label_cnpj.pack()
    entry_cnpj = tk.Entry(popup)
    entry_cnpj.pack()

    label_inscricao_estadual = tk.Label(popup, text='Inscrição Estadual:')
    label_inscricao_estadual.pack()
    entry_inscricao_estadual = tk.Entry(popup)
    entry_inscricao_estadual.pack()

    label_inscricao_municipal = tk.Label(popup, text='Inscrição Municipal:')
    label_inscricao_municipal.pack()
    entry_inscricao_municipal = tk.Entry(popup)
    entry_inscricao_municipal.pack()

    label_rua = tk.Label(popup, text='Rua:')
    label_rua.pack()
    entry_rua = tk.Entry(popup)
    entry_rua.pack()

    label_bairro = tk.Label(popup, text='Bairro:')
    label_bairro.pack()
    entry_bairro = tk.Entry(popup)
    entry_bairro.pack()

    label_cidade = tk.Label(popup, text='Cidade:')
    label_cidade.pack()
    entry_cidade = tk.Entry(popup)
    entry_cidade.pack()

    label_estado = tk.Label(popup, text='Estado:')
    label_estado.pack()
    entry_estado = tk.Entry(popup)
    entry_estado.pack()

    label_cep = tk.Label(popup, text='CEP:')
    label_cep.pack()
    entry_cep = tk.Entry(popup)
    entry_cep.pack()

    label_observacoes = tk.Label(popup, text='Observações:')
    label_observacoes.pack()
    entry_observacoes = tk.Entry(popup)
    entry_observacoes.pack()

    # Botão para salvar os dados do fornecedor
    btn_salvar = tk.Button(popup, text='Salvar', command=lambda: salvar_fornecedor(entry_nome_fantasia.get(),
                                                                                  entry_razao_social.get(),
                                                                                  entry_cnpj.get(),
                                                                                  entry_inscricao_estadual.get(),
                                                                                  entry_inscricao_municipal.get(),
                                                                                  entry_rua.get(),
                                                                                  entry_bairro.get(),
                                                                                  entry_cidade.get(),
                                                                                  entry_estado.get(),
                                                                                  entry_cep.get(),
                                                                                  entry_observacoes.get()))
    btn_salvar.pack()

# Função para salvar os dados do fornecedor no banco de dados
def salvar_fornecedor(nome_fantasia, razao_social, cnpj, inscricao_estadual, inscricao_municipal, rua, bairro, cidade, estado, cep, observacoes):
    # Conecta ao banco de dados
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()

    # Insere os dados do fornecedor na tabela "fornecedor"
    cursor.execute('''INSERT INTO fornecedor (nome_fantasia, razao_social, cnpj, inscricao_estadual, inscricao_municipal, rua, bairro, cidade, estado, cep, observacoes)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (nome_fantasia, razao_social, cnpj, inscricao_estadual, inscricao_municipal, rua, bairro, cidade, estado, cep, observacoes))

    # Comita as alterações
    conn.commit()

    # Fecha a conexão com o banco de dados
    conn.close()


# Função para abrir a janela de cadastro de categoria
def abrir_cadastro_categoria():
    popup = tk.Toplevel(root)
    popup.title('Cadastro de Categoria')

    # Campo de entrada para cadastrar a categoria
    label_categoria = tk.Label(popup, text='Categoria:')
    label_categoria.pack()
    entry_categoria = tk.Entry(popup)
    entry_categoria.pack()

    # Botão para salvar os dados da categoria
    btn_salvar_categoria = tk.Button(popup, text='Salvar', command=lambda: salvar_categoria(entry_categoria.get()))
    btn_salvar_categoria.pack()

# Função para salvar os dados da categoria no banco de dados
def salvar_categoria(categoria):
    # Conecta ao banco de dados
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()

    # Insere o nome da categoria na tabela "categoria"
    cursor.execute('''INSERT INTO categoria (categoria)
                      VALUES (?)''',
                   (categoria,))

    # Comita as alterações
    conn.commit()

    # Fecha a conexão com o banco de dados
    conn.close()


# Cria a janela da interface de listagem de produtos
def criar_lista_produtos():
    global root,tree

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


# Vincular o evento de duplo clique na árvore (Treeview) para exibir detalhes do produto
    tree.bind("<Double-1>", exibir_detalhes_produto)

 # Botão para abrir a janela de cadastro de produto
    btn_cadastrar_produto = tk.Button(root, text='Cadastro de Produto', command=abrir_interface_cadastro)
    btn_cadastrar_produto.grid(row=1, column=0, padx=5, pady=5)

# Botão para abrir a janela de cadastro de fornecedor
    btn_cadastrar_fornecedor = tk.Button(root, text='Cadastrar Fornecedor', command=abrir_cadastro_fornecedor)
    btn_cadastrar_fornecedor.grid(row=1, column=1, padx=5, pady=5)

   # Botão para abrir a janela de cadastro de categoria
    btn_cadastrar_categoria = tk.Button(root, text='Cadastrar Categoria', command=abrir_cadastro_categoria)
    btn_cadastrar_categoria.grid(row=1, column=2, padx=5, pady=5)


    root.mainloop()

# Função para abrir a janela de cadastro de produtos (interface.py)
def abrir_interface_cadastro():
    import interface

# Chama a função para criar a interface de listagem de produtos
if __name__ == "__main__":
    criar_lista_produtos()