import unittest
import tkinter as tk
from tela_login import TelaLogin

class TestTelaLogin(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.tela_principal = tk.Toplevel(self.root)
        self.login = TelaLogin(self.root, self.tela_principal)

    def tearDown(self):
        self.root.destroy()

    def test_labels_and_entries(self):
        # Verifica se os widgets foram criados corretamente
        self.assertIsInstance(self.login.label_usuario, tk.Label)
        self.assertIsInstance(self.login.entry_usuario, tk.Entry)

    def test_login_functionality(self):
        # Simula a entrada do usuário e verifica o comportamento do login
        self.login.entry_usuario.insert(0, "admin")
        self.login.entry_senha.insert(0, "admin")
        # Aqui você pode adicionar mais lógica para simular o clique no botão de login e verificar o resultado

if __name__ == '__main__':
    unittest.main()