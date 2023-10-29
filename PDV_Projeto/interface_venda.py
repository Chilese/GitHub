import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime  # Importe o módulo datetime

class PDVInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("PDV - Ponto de Venda")

        # Variáveis
        self.cliente_cpf = tk.StringVar()
        self.forma_pagamento = tk.StringVar()
        self.produtos = []

        # Layout
        label_cpf = tk.Label(root, text="CPF do Cliente:")
        label_cpf.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        entry_cpf = tk.Entry(root, textvariable=self.cliente_cpf)
        entry_cpf.grid(row=0, column=1, padx=10, pady=10)

        label_pagamento = tk.Label(root, text="Forma de Pagamento:")
        label_pagamento.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        combo_pagamento = ttk.Combobox(root, textvariable=self.forma_pagamento, values=["Débito", "Crédito", "Dinheiro"])
        combo_pagamento.grid(row=1, column=1, padx=10, pady=10)

        label_produtos = tk.Label(root, text="Produtos:")
        label_produtos.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.combo_produtos = ttk.Combobox(root, values=self.obter_nomes_produtos())
        self.combo_produtos.grid(row=2, column=1, padx=10, pady=10)
        self.combo_produtos.bind("<Return>", self.adicionar_produto)

        self.lista_produtos = ttk.Treeview(root, columns=("Nome", "Preço", "Quantidade", "Total"))
        self.lista_produtos.heading("#1", text="Nome")
        self.lista_produtos.heading("#2", text="Preço")
        self.lista_produtos.heading("#3", text="Quantidade")
        self.lista_produtos.heading("#4", text="Total")
        self.lista_produtos.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='w')
        self.lista_produtos.bind("<Double-1>", self.editar_quantidade)

        label_total = tk.Label(root, text="Total da Compra:")
        label_total.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.total_label = tk.Label(root, text="R$ 0.00")
        self.total_label.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        #Botão finalizar a compra
        finalizar_compra_button = tk.Button(root, text="Finalizar Compra", command=self.finalizar_compra)
        finalizar_compra_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky= 'e')

    def obter_nomes_produtos(self):
        # Conectar ao banco de dados
         conexao = sqlite3.connect("estoque.db")
         cursor = conexao.cursor()

         # Obtenha os nomes de todos os produtos
         cursor.execute("SELECT nome FROM estoque")
         nomes_produtos = cursor.fetchall()

         # Feche a conexão
         conexao.close()

         # Retorne os nomes de produtos
         return [produto[0] for produto in nomes_produtos]

    def adicionar_produto(self, event=None):
        produto = self.combo_produtos.get()
        
        # Conectar ao banco de dados
        conexao = sqlite3.connect("estoque.db")
        cursor = conexao.cursor()

        #Executar a consulta SQL para preço
        cursor.execute("SELECT preco_venda FROM estoque WHERE nome = ?", (produto,))
        preco = cursor.fetchone()[0]

        #Fechar a conexão com o banco de dados
        conexao.close()

        quantidade = 1
        total = preco * quantidade

        # Adicione o produto à lista de produtos
        self.produtos.append({"nome": produto, "preco": preco, "quantidade": quantidade, "total": total})

        # Adicione o produto à Treeview
        self.lista_produtos.insert("", "end", values=(produto, f"R$ {preco:.2f}", quantidade, f"R$ {total:.2f}"))

        # Atualize o total da compra
        self.atualizar_total()

        # Limpe o campo de seleção de produtos
        self.combo_produtos.set("")

    def editar_quantidade(self, event):
        item = self.lista_produtos.selection()[0]
        produto_index = int(item.split("I")[1]) - 1

        # Obtenha a quantidade atual do produto
        quantidade_atual = self.produtos[produto_index]["quantidade"]

        # Crie uma janela para editar a quantidade
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Editar Quantidade")

        label_quantidade = tk.Label(edit_window, text="Quantidade:")
        label_quantidade.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        entry_quantidade = tk.Entry(edit_window)
        entry_quantidade.insert(0, quantidade_atual)
        entry_quantidade.grid(row=0, column=1, padx=10, pady=10)

        # Função para atualizar a quantidade
        def salvar_quantidade():
            nova_quantidade = int(entry_quantidade.get())
            self.produtos[produto_index]["quantidade"] = nova_quantidade
            self.lista_produtos.item(item, values=(self.produtos[produto_index]["nome"],
                                                   f"R$ {self.produtos[produto_index]['preco']:.2f}",
                                                   nova_quantidade,
                                                   f"R$ {self.produtos[produto_index]['preco'] * nova_quantidade:.2f}"))
            edit_window.destroy()
            self.atualizar_total()

        # Botão para salvar a quantidade
        btn_salvar = tk.Button(edit_window, text="Salvar", command=salvar_quantidade)
        btn_salvar.grid(row=1, column=0, columnspan=2, pady=10)

    def atualizar_total(self):
        # Calcule o total da compra somando os valores totais dos produtos
        total_compra = sum(produto["preco"] * produto["quantidade"] for produto in self.produtos)
        self.total_label.config(text=f"R$ {total_compra:.2f}")

    def finalizar_compra(self):
        # 1. Registrar a venda no banco de dados
        cpf_cliente = self.cliente_cpf.get()
        forma_pagamento = self.forma_pagamento.get()
        total_compra = float(self.total_label.cget("text").replace("R$ ", ""))  # Obtém o total da compra
        data_hora_venda = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtém a data e hora atual

        # Conecta ao banco de dados e insere os dados na tabela "vendas"
        conn = sqlite3.connect("estoque.db")
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO vendas (cpf_cliente, forma_pagamento, total_compra, data_hora_venda)
                      VALUES (?, ?, ?, ?)''', (cpf_cliente, forma_pagamento, total_compra, data_hora_venda))
        conn.commit()

        # 2. Atualizar estoque com a quantidade vendida
        for produto in self.produtos:
            nome_produto = produto["nome"]
            quantidade_vendida = produto["quantidade"]

            # Conecta ao banco de dados e atualiza a quantidade do produto vendido
            cursor.execute("UPDATE estoque SET quantidade = quantidade - ? WHERE nome = ?", (quantidade_vendida, nome_produto))
            conn.commit()

        # 3. Limpar dados de venda atual
        self.cliente_cpf.set("")
        self.forma_pagamento.set("")
        self.produtos.clear()
        self.lista_produtos.delete(*self.lista_produtos.get_children()) 
        self.total_label.config(text="R$ 0.00")

        messagebox.showinfo("Compra Finalizada", "Compra registrada om sucesso!")

        conn.close()

# Criar a janela principal
root = tk.Tk()
pdv_interface = PDVInterface(root)
root.mainloop()
