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

# Diretório dos ícones
icon_dir = os.path.join(os.path.dirname(__file__), "icons")

# Lista de novos scripts a serem abertos com ícones correspondentes
scripts = [
    {"nome": "Cadastro de Produtos", "script": "cadastro_produtos", "icone": os.path.join(icon_dir, "produtos.png")},
    {"nome": "Gestão de Estoque", "script": "gestao_estoque", "icone": os.path.join(icon_dir, "estoque.png")},
    {"nome": "Cadastro de Fornecedores", "script": "cadastro_fornecedores", "icone": os.path.join(icon_dir, "fornecedores.png")},
    {"nome": "Gestão de Vendas", "script": "gestao_vendas", "icone": os.path.join(icon_dir, "vendas.png")}
]

# Função para criar botões com ícones e textos
def criar_botao(script):
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(side=tk.LEFT, padx=10, pady=10)

    # Verifica se o ícone existe
    if not os.path.exists(script["icone"]):
        print(f"Ícone não encontrado: {script['icone']}")
        return

    img = Image.open(script["icone"])
    img = img.resize((button_width, button_height), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)

    botao = tk.Button(frame, image=photo, command=lambda: abrir_script(script["script"]))
    botao.image = photo  # Manter uma referência da imagem para evitar garbage collection
    botao.pack()

    label = tk.Label(frame, text=script["nome"], wraplength=button_width, justify=tk.CENTER)
    label.pack()

# Criar botões para cada script
for script in scripts:
    criar_botao(script)

root.mainloop()