import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import os

def abrir_script(script_nome):
    script_path = os.path.join(os.path.dirname(__file__), f"{script_nome}.py")
    subprocess.run(["python", script_path])

root = tk.Tk()
root.title('Bem-vindo ao Seu Sistema PDV')

# Tamanho padrão para os botões
button_width = 150
button_height = 150

# Lista de scripts a serem abertos com ícones correspondentes
scripts = [
    {"nome": "Cadastro de Produto", "script": "cadastro_produto", "icone": "produto.png"},
    {"nome": "Cadastro de Fornecedor", "script": "cadastro_fornecedor", "icone": "fornecedor.png"},
    {"nome": "Cadastro de Categoria", "script": "cadastro_categoria", "icone": "categoria.png"},
    {"nome": "Visualizar Estoque", "script": "tela_estoque_revisado", "icone": "estoque.png"}
]

# Frames para organizar os botões
frame_top = tk.Frame(root)
frame_bottom = tk.Frame(root)

# Funções para abrir os scripts
for i, script_info in enumerate(scripts):
    # Carregar ícone
    icon_path = os.path.join(os.path.dirname(__file__), f"icons/{script_info['icone']}")
    icon = Image.open(icon_path)

    # Redimensionar imagem
    icon = icon.resize((button_width - 20, button_height - 50))

    # Converter para o formato Tkinter
    icon = ImageTk.PhotoImage(icon)

    # Adicionar botão com ícone e descrição
    btn = tk.Button(frame_top if i < 2 else frame_bottom, text=script_info["nome"], image=icon, compound="top", command=lambda s=script_info["script"]: abrir_script(s), width=button_width, height=button_height)
    btn.image = icon  # Manter referência ao ícone para evitar que seja coletado pelo garbage collector
    btn.pack(side=tk.LEFT if i % 2 == 0 else tk.RIGHT, padx=10)

# Empacotar os frames
frame_top.pack(pady=10)
frame_bottom.pack(pady=10)

# Inicia a execução da interface
root.mainloop()
