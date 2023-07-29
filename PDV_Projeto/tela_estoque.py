import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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

# Função para abrir a janela de cadastro de produtos (interface.py)
def abrir_interface_cadastro():
    import interface

# Função para abrir a janela de edição do produto
def editar_produto(event):
    # Obtenha o item selecionado na árvore
    item_id = tree.selection()[0]
    
    # Obtenha os valores atuais do produto com base no item_id
    valores = tree.item(item_id, 'values')

    # Crie uma janela pop-up para edição
    popup = tk.Toplevel(root)
    popup.title('Editar Produto')

    # Adicione campos de entrada para a edição dos detalhes do produto
    # Preencha esses campos com os valores atuais

    # Nome
    label_nome = tk.Label(popup, text='Nome:')
    label_nome.pack()
    entry_nome = tk.Entry(popup)
    entry_nome.insert(0, valores[1])  # Insira o valor atual
    entry_nome.pack()

    # Descrição
    label_descricao = tk.Label(popup, text='Descrição:')
    label_descricao.pack()
    entry_descricao = tk.Entry(popup)
    entry_descricao.insert(0, valores[2])  # Insira o valor atual
    entry_descricao.pack()

    # Categoria (você pode adicionar campos semelhantes para outros atributos)
    label_categoria = tk.Label(popup, text='Categoria:')
    label_categoria.pack()
    entry_categoria = tk.Entry(popup)
    entry_categoria.insert(0, valores[3])  # Insira o valor atual
    entry_categoria.pack()

    # Preço de Compra(você pode adicionar campos semelhantes para outros atributos)
    label_preco_compra = tk.Label(popup, text='Preço de Compra:')
    label_preco_compra.pack()
    entry_preco_compra  = tk.Entry(popup)
    entry_preco_compra.insert(0, valores[4])  # Insira o valor atual
    entry_preco_compra.pack()

    # Preço de Venda (você pode adicionar campos semelhantes para outros atributos)
    label_preco_venda = tk.Label(popup, text='Preço de Venda:')
    label_preco_venda.pack()
    entry_preco_venda  = tk.Entry(popup)
    entry_preco_venda.insert(0, valores[5])  # Insira o valor atual
    entry_preco_venda.pack()

    # Quantidade (você pode adicionar campos semelhantes para outros atributos)
    label_quantidade = tk.Label(popup, text='Quantidade:')
    label_quantidade.pack()
    entry_quantidade  = tk.Entry(popup)
    entry_quantidade.insert(0, valores[6])  # Insira o valor atual
    entry_quantidade.pack()

    # Data de Entrada
    label_data_entrada = tk.Label(popup, text='Data de Entrada:')
    label_data_entrada.pack()
    entry_data_entrada   = tk.Entry(popup)
    entry_data_entrada.insert(0, valores[7])
    entry_data_entrada.pack()

    # Fornecedor
    label_fornecedor= tk.Label(popup, text='Fornecedor:')
    label_fornecedor.pack()
    entry_fornecedor  =  tk.Entry(popup)
    entry_fornecedor.insert(0, valores[8])
    entry_fornecedor.pack()

    # Notas
    label_notas = tk.Label(popup, text='Notas:')
    label_notas.pack()
    entry_notas  = tk.Entry(popup)
    entry_notas.insert(0, valores[9])
    entry_notas.pack()

    # Botão para salvar as edições
    btn_salvar = tk.Button(popup, text='Salvar Edições', command=lambda: salvar_edicoes(item_id, entry_nome.get(), entry_descricao.get(), entry_categoria.get(), entry_preco_compra.get(), entry_preco_venda.get(), entry_quantidade.get(), entry_data_entrada.get(), entry_fornecedor.get(), entry_notas.get()))
    btn_salvar.pack()

# Função para salvar as edições do produto
def salvar_edicoes(item_id, novo_nome, nova_descricao, nova_categoria, novo_preco_compra, novo_preco_venda, nova_quantidade, nova_data_entrada, novo_fornecedor, novas_notas):
    # Atualize os detalhes do produto no banco de dados com base no item_id
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE estoque SET nome = ?, descricao = ?, categoria = ?, preco_compra = ?, preco_venda = ?, quantidade = ?, data_entrada = ?, notas = ? WHERE id = ?''', (novo_nome, nova_descricao, nova_categoria, novo_preco_compra, novo_preco_venda, nova_quantidade, nova_data_entrada, novas_notas, item_id))
    conn.commit()
    conn.close()

    # Atualize a exibição na árvore (Treeview)
    tree.item(item_id, values=(item_id, novo_nome, nova_descricao, nova_categoria, novo_preco_compra, novo_preco_venda, nova_quantidade, nova_data_entrada, novo_fornecedor, novas_notas))

# Função para excluir o produto
def excluir_produto():
    # Obtenha o ID do produto selecionado na árvore
    item_id = tree.selection()[0]

    if item_id:
        # Exibir uma mensagem de confirmação antes da exclusão
        resultado = messagebox.askquestion('Excluir Produto', 'Você tem certeza que deseja excluir este produto?')

        if resultado == 'yes':
            try:
                # Conectar ao banco de dados
                conn = sqlite3.connect('estoque.db')
                cursor = conn.cursor()

                # Executar a consulta SQL DELETE para remover o produto
                cursor.execute('''DELETE FROM estoque WHERE id = ?''', (item_id,))

                # Confirmar a transação
                conn.commit()

                # Fechar a conexão com o banco de dados
                conn.close()

                # Remover o produto da árvore
                tree.delete(item_id)
            except sqlite3.Error as e:
                messagebox.showerror('Erro', f'Erro ao excluir o produto: {e}')


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

    # Configura a função para lidar com a abertura da janela de edição
    tree.bind("<Double-1>", editar_produto)

    # Botão para excluir o produto
    btn_excluir = tk.Button(root, text="Excluir Produto", command=excluir_produto)
    btn_excluir.grid(row=1, column=0, padx=10, pady=10)

    root.mainloop()
