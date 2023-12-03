import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns  # Importe Seaborn
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard - PDV")

        # Conectar ao banco de dados
        self.conn = sqlite3.connect("estoque.db")
        self.cursor = self.conn.cursor()

        # Layout
        self.create_widgets()

    def create_widgets(self):
        # Crie um notebook para organizar diferentes guias para cada gráfico
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Adicione cada gráfico como uma guia separada no notebook
        self.add_tab(notebook, "Total de Vendas por Período", self.show_total_vendas_periodo)
        self.add_tab(notebook, "Total de Vendas por Forma de Pagamento", self.show_vendas_forma_pagamento)
        self.add_tab(notebook, "Ticket Médio", self.show_ticket_medio)
        self.add_tab(notebook, "Produtos Mais Vendidos", self.show_produtos_mais_vendidos)
        self.add_tab(notebook, "Margem de Lucro", self.show_margem_lucro)
        self.add_tab(notebook, "Distribuição de Vendas por Horário", self.show_distribuicao_vendas_horario)
        self.add_tab(notebook, "Vendas por Categoria de Produto", self.show_vendas_por_categoria)

    def add_tab(self, notebook, title, func):
        # Crie uma nova guia no notebook
        tab = ttk.Frame(notebook)
        notebook.add(tab, text=title)

        # Chame a função passada para criar o gráfico na guia
        func(tab)

    def execute_query(self, query, parameters=None):
        if parameters:
            self.cursor.execute(query, parameters)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def show_total_vendas_periodo(self, tab):
        query = "SELECT strftime('%Y-%m-%d', data_hora_venda) as data, SUM(total_compra) FROM vendas GROUP BY data"
        data = self.execute_query(query)

        if not data:
            messagebox.showinfo("Aviso", "Não há dados disponíveis para o indicador 'Total de Vendas por Período'.")
            return

        datas, valores = zip(*data)
        fig, ax = plt.subplots()
        ax.plot(datas, valores, marker='o')
        ax.set_title('Total de Vendas por Período')
        ax.set_xlabel('Período')
        ax.set_ylabel('Total de Vendas (R$)')
        self.show_graph(fig, tab)

    def show_vendas_forma_pagamento(self, tab):
        query = "SELECT forma_pagamento, SUM(total_compra) FROM vendas GROUP BY forma_pagamento"
        data = self.execute_query(query)

        if not data:
            messagebox.showinfo("Aviso", "Não há dados disponíveis para o indicador 'Total de Vendas por Forma de Pagamento'.")
            return

        formas, valores = zip(*data)
        fig, ax = plt.subplots()
        ax.pie(valores, labels=formas, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title('Distribuição de Vendas por Forma de Pagamento')
        self.show_graph(fig, tab)

    def show_ticket_medio(self, tab):
        query = "SELECT strftime('%Y-%m-%d', data_hora_venda) as data, AVG(total_compra) FROM vendas GROUP BY data"
        data = self.execute_query(query)

        if not data:
            messagebox.showinfo("Aviso", "Não há dados disponíveis para o indicador 'Ticket Médio'.")
            return

        datas, valores = zip(*data)
        fig, ax = plt.subplots()
        ax.plot(datas, valores, marker='o')
        ax.set_title('Ticket Médio por Período')
        ax.set_xlabel('Período')
        ax.set_ylabel('Ticket Médio (R$)')
        self.show_graph(fig, tab)

    def show_produtos_mais_vendidos(self, tab):
        query = "SELECT produto_nome, SUM(quantidade) FROM itens_venda GROUP BY produto_nome"
        data = self.execute_query(query)

        if not data:
            messagebox.showinfo("Aviso", "Não há dados disponíveis para o indicador 'Produtos Mais Vendidos'.")
            return

        produtos, quantidades = zip(*data)
        fig, ax = plt.subplots()
        ax.bar(produtos, quantidades)
        ax.set_title('Produtos Mais Vendidos')
        ax.set_xlabel('Produto')
        ax.set_ylabel('Quantidade Vendida')
        plt.xticks(rotation=45, ha="right")
        self.show_graph(fig, tab)

    def show_margem_lucro(self, tab):
        query = "SELECT strftime('%Y-%m-%d', v.data_hora_venda) as data, " \
                "SUM(e.preco_venda - e.preco_compra) / SUM(e.preco_compra) * 100 " \
                "FROM vendas v JOIN itens_venda i ON v.id = i.venda_id " \
                "JOIN estoque e ON i.produto_nome = e.nome GROUP BY data"
        data = self.execute_query(query)

        if not data:
            messagebox.showinfo("Aviso", "Não há dados disponíveis para o indicador 'Margem de Lucro'.")
            return

        datas, margens = zip(*data)
        fig, ax = plt.subplots()
        ax.plot(datas, margens, marker='o')
        ax.set_title('Margem de Lucro por Período')
        ax.set_xlabel('Período')
        ax.set_ylabel('Margem de Lucro (%)')
        self.show_graph(fig, tab)

    def show_distribuicao_vendas_horario(self, tab):
        query = "SELECT strftime('%H', data_hora_venda) as hora, COUNT(*) FROM vendas GROUP BY hora"
        data = self.execute_query(query)

        if not data:
            messagebox.showinfo("Aviso", "Não há dados disponíveis para o indicador 'Distribuição de Vendas por Horário'.")
            return

        horas, vendas = zip(*data)
        fig, ax = plt.subplots()
        ax.bar(horas, vendas)
        ax.set_title('Distribuição de Vendas por Horário')
        ax.set_xlabel('Hora do Dia')
        ax.set_ylabel('Número de Vendas')
        self.show_graph(fig, tab)

    def show_vendas_por_categoria(self, tab):
        query = "SELECT c.categoria, SUM(e.preco_venda * i.quantidade) " \
                "FROM itens_venda i JOIN estoque e ON i.produto_nome = e.nome " \
                "JOIN categoria c ON e.categoria_id = c.categoria_id GROUP BY c.categoria"
        data = self.execute_query(query)

        if not data:
            messagebox.showinfo("Aviso", "Não há dados disponíveis para o indicador 'Vendas por Categoria de Produto'.")
            return

        categoria, vendas = zip(*data)
        fig, ax = plt.subplots()
        ax.pie(vendas, labels=categoria, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title('Vendas por Categoria de Produto')

        # Use Seaborn para melhorar a estética
        sns.set()
        sns.despine()
        sns.set_palette("pastel")
        plt.show()  # Mostra o gráfico utilizando o Seaborn

    def show_graph(self, fig, tab):
        # Cria um widget do Tkinter para exibir o gráfico
        canvas = FigureCanvasTkAgg(fig, master=tab)
        canvas.draw()
        canvas.get_tk_widget().pack()

# Função principal
def main():
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
