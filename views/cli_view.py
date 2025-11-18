from controllers.senha_controller import ExecutarControllers
from models.password_models import SenhaModel
import os



class CliView():
    def __init__(self):
        self.controle = ExecutarControllers()
        self.senha_model = SenhaModel()

    def app(self):
        while True:
            self.menu()
            escolha = input("Digite uma das opções [1, 2, Q]").lower()
            if len(escolha) > 1 and escolha not in ['q', '1', '2']:
                print("Opção inválida. Tente novamente.")
            elif escolha == '1':
                self.criar_senha()
            elif escolha == '2':
                self.controle.listar_senhas()
            elif escolha == 'q':
                print("Saindo...")
                break

            

    def menu(self):
        """Exibe as opções disponíveis para o usuário."""
        print("\n--- Gerenciador de Senhas CLI ---")
        print("1. Criar nova senha")
        print("2. Listar senhas")
        print("Q. Sair")
        print("---------------------------------")    


    def criar_senha(self):
        self.controle.main()

            