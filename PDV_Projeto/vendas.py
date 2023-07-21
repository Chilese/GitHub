import sqlite3
from datetime import datetime

# Função para registrar uma venda
def registrar_venda(id_produto, quantidade, forma_pagamento):
    # Conecta-se ao banco de dados de vendas
    conn_vendas = sqlite3.connect('vendas.db')
    cursor_vendas = conn_vendas.cursor()

    # Obtém as informações do produto a partir do estoque.db
    conn_estoque = sqlite3.connect('estoque.db')
    cursor_estoque = conn_estoque.cursor()
    cursor_estoque.execute("SELECT nome, preco_venda FROM estoque WHERE id=?", (id_produto,))
    produto = cursor_estoque.fetchone()
    nome_produto = produto[0]
    preco_venda = produto[1]

    # Calcula o valor total da venda
    valor_venda = preco_venda * quantidade

    # Obtém a data e hora atuais
    data_venda = datetime.now().strftime('%d/%m/%Y')
    hora_venda = datetime.now().strftime('%H:%M:%S')

    # Insere os dados da venda no banco de dados de vendas
    cursor_vendas.execute("INSERT INTO vendas (id_produto, nome_produto, quantidade, forma_pagamento, preco_venda, data_venda, hora_venda, valor_venda) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                          (id_produto, nome_produto, quantidade, forma_pagamento, preco_venda, data_venda, hora_venda, valor_venda))
    conn_vendas.commit()

    # Atualiza a quantidade do produto no banco de dados de estoque
    cursor_estoque.execute("UPDATE estoque SET quantidade = quantidade - ? WHERE id = ?", (quantidade, id_produto))
    conn_estoque.commit()

    # Fecha as conexões com os bancos de dados
    conn_vendas.close()
    conn_estoque.close()

# Exemplo de uso: registrar uma venda
id_produto = 1  # ID do produto vendido
quantidade = 2  # Quantidade vendidaimport sqlite3
from datetime import datetime

# Função para registrar uma venda
def registrar_venda(id_produto, quantidade, forma_pagamento):
    # Conecta-se ao banco de dados de vendas
    conn_vendas = sqlite3.connect('vendas.db')
    cursor_vendas = conn_vendas.cursor()

    # Obtém as informações do produto a partir do estoque.db
forma_pagamento = "Débito"  # Forma de pagamento

registrar_venda(id_produto, quantidade, forma_pagamento)
forma_pagamento = "Débito"  # Forma de pagamento

registrar_venda(id_produto, quantidade, forma_pagamento)