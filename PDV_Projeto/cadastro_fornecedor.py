import tkinter as tk
from tkinter import messagebox  # Importe o módulo messagebox
import sqlite3

def abrir_cadastro_fornecedor():
    # Campo de entrada para cadastrar o fornecedor
    label_nome_fantasia = tk.Label(root, text='Nome Fantasia:')
    label_nome_fantasia.pack()
    entry_nome_fantasia = tk.Entry(root)
    entry_nome_fantasia.pack()

    label_razao_social = tk.Label(root, text='Razão Social:')
    label_razao_social.pack()
    entry_razao_social = tk.Entry(root)
    entry_razao_social.pack()

    label_cnpj = tk.Label(root, text='CNPJ:')
    label_cnpj.pack()
    entry_cnpj = tk.Entry(root)
    entry_cnpj.pack()

    label_inscricao_estadual = tk.Label(root, text='Inscrição Estadual:')
    label_inscricao_estadual.pack()
    entry_inscricao_estadual = tk.Entry(root)
    entry_inscricao_estadual.pack()

    label_inscricao_municipal = tk.Label(root, text='Inscrição Municipal:')
    label_inscricao_municipal.pack()
    entry_inscricao_municipal = tk.Entry(root)
    entry_inscricao_municipal.pack()

    label_rua = tk.Label(root, text='Rua:')
    label_rua.pack()
    entry_rua = tk.Entry(root)
    entry_rua.pack()

    label_bairro = tk.Label(root, text='Bairro:')
    label_bairro.pack()
    entry_bairro = tk.Entry(root)
    entry_bairro.pack()

    label_cidade = tk.Label(root, text='Cidade:')
    label_cidade.pack()
    entry_cidade = tk.Entry(root)
    entry_cidade.pack()

    label_estado = tk.Label(root, text='Estado:')
    label_estado.pack()
    entry_estado = tk.Entry(root)
    entry_estado.pack()

    label_cep = tk.Label(root, text='CEP:')
    label_cep.pack()
    entry_cep = tk.Entry(root)
    entry_cep.pack()

    label_observacoes = tk.Label(root, text='Observações:')
    label_observacoes.pack()
    entry_observacoes = tk.Entry(root)
    entry_observacoes.pack()

    # Botão para salvar os dados do fornecedor
    btn_salvar = tk.Button(root, text='Salvar', command=lambda: salvar_fornecedor(
        entry_nome_fantasia.get(),
        entry_razao_social.get(),
        entry_cnpj.get(),
        entry_inscricao_estadual.get(),
        entry_inscricao_municipal.get(),
        entry_rua.get(),
        entry_bairro.get(),
        entry_cidade.get(),
        entry_estado.get(),
        entry_cep.get(),
        entry_observacoes.get()
    ))
    btn_salvar.pack()

def salvar_fornecedor(nome_fantasia, razao_social, cnpj, inscricao_estadual, inscricao_municipal, rua, bairro, cidade, estado, cep, observacoes):
    # Conecta ao banco de dados
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()

    try:
        # Insere os dados do fornecedor na tabela "fornecedor"
        cursor.execute('''INSERT INTO fornecedor (nome_fantasia, razao_social, cnpj, inscricao_estadual, inscricao_municipal, rua, bairro, cidade, estado, cep, observacoes)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (nome_fantasia, razao_social, cnpj, inscricao_estadual, inscricao_municipal, rua, bairro, cidade, estado, cep, observacoes))

        # Comita as alterações
        conn.commit()

        # Exiba uma mensagem de confirmação
        messagebox.showinfo('Sucesso', 'Fornecedor cadastrado com sucesso!')
    except sqlite3.Error as e:
        # Em caso de erro, exiba uma mensagem de erro
        messagebox.showerror('Erro', 'Erro ao cadastrar fornecedor: ' + str(e))
    finally:
        # Fecha a conexão com o banco de dados
        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Cadastro de Fornecedor')

    abrir_cadastro_fornecedor()

    root.mainloop()