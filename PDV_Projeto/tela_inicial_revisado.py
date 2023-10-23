import tkinter as tk
import subprocess

# Funções para chamar os códigos correspondentes aos botões
def abrir_cadastro_produto():
    subprocess.run(["python3", "interface.py"], cwd="/home/chilese/Documentos/GitHub/PDV_Projeto")

def abrir_cadastro_fornecedor():
    subprocess.run(["python3", "cadastro_fornecedor.py"], cwd="/home/chilese/Documentos/GitHub/PDV_Projeto")

def abrir_cadastro_categoria():
    subprocess.run(["python3", "cadastro_categoria.py"], cwd="/home/chilese/Documentos/GitHub/PDV_Projeto")

def abrir_visualizar_estoque():
    subprocess.run(["python3", "tela_estoque_revisado.py"], cwd="/home/chilese/Documentos/GitHub/PDV_Projeto")

# Cria a janela da interface
root = tk.Tk()
root.title('Home - Bem vindo!')

# Funções para abrir as interfaces correspondentes
btn_produto = tk.Button(root, text='Cadastro de Produto', command=abrir_cadastro_produto)
btn_produto.pack(pady=10)

btn_fornecedor = tk.Button(root, text='Cadastro de Fornecedor', command=abrir_cadastro_fornecedor)
btn_fornecedor.pack(pady=10)

btn_categoria = tk.Button(root, text='Cadastro de Categoria', command=abrir_cadastro_categoria)
btn_categoria.pack(pady=10)

btn_estoque = tk.Button(root, text='Visualizar Estoque', command=abrir_visualizar_estoque)
btn_estoque.pack(pady=10)

# Inicia a execução da interface
root.mainloop()
