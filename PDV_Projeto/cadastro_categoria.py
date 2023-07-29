import tkinter as tk
from tkinter import messagebox
import sqlite3

def salvar_categoria(categoria):
    # Conecta ao banco de dados
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()

    try:
        # Insere o nome da categoria na tabela "categoria"
        cursor.execute('''INSERT INTO categoria (categoria)
                            VALUES (?)''',
                        (categoria,))
            
        # Comita as alterações
        conn.commit()

            # Exiba uma mensagem de confirmação
        messagebox.showinfo('Sucesso', 'Categoria inserida com sucesso!')
    except sqlite3.Error as e:
        # Em caso de erro, exiba uma mensagem de erro
        messagebox.showerror('Erro', 'Erro ao inserir categoria: ' + str(e))
    finally:
        # Feche a conexão com o banco de dados
        conn.close()

   
if __name__ == "__main__":
    root = tk.Tk()
    root.title('Cadastro de Categoria')

    # Campo de entrada para cadastrar a categoria
    label_categoria = tk.Label(root, text='Categoria:')
    label_categoria.pack()
    entry_categoria = tk.Entry(root)
    entry_categoria.pack()

    # Botão para salvar os dados da categoria
    btn_salvar_categoria = tk.Button(root, text='Salvar', command=lambda: salvar_categoria(entry_categoria.get()))
    btn_salvar_categoria.pack()

    root.mainloop()
