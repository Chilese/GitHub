import tkinter as tk
import subprocess
import os

def abrir_script(script_nome):
    script_path = os.path.join(os.path.dirname(__file__), f"{script_nome}.py")
    subprocess.run(["python", script_path])

# Cria a janela da interface
root = tk.Tk()
root.title('Home - Bem-vindo!')

# Lista de scripts a serem abertos
scripts = ["cadastro_produto", "cadastro_fornecedor", "cadastro_categoria", "tela_estoque_revisado"]

# Funções para abrir os scripts
for script in scripts:
    btn = tk.Button(root, text=f'Abrir {script.replace("_", " ")}', command=lambda s=script: abrir_script(s))
    btn.pack(pady=10)

# Inicia a execução da interface
root.mainloop()
