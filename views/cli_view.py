from controllers.senha_controller import ExecutarControllers
from models.password_models import SenhaModel
from models.criptografar_arquivo import CriptArquivojson
from models.criar_bd import SenhasLoginsJson
import os



class CliView():
    def __init__(self):
        self.controle = ExecutarControllers()
        self.senha_model = SenhaModel()
        self.bd = SenhasLoginsJson()

    def app(self):
        cript_arquivo_json = CriptArquivojson()

        while True:
            self.menu()
            escolha = input("Digite uma das opções [1, 2, 3, 4, Q]: ").lower()
            if len(escolha) > 1 and escolha not in ['q', '1', '2']:
                print("Opção inválida. Tente novamente.")
            elif escolha == '1':
                try:
                    self.criar_senha()
                    print("Deseja criptografar o arquivo gerado? (s/n)")
                    resposta = input().lower()
                    if resposta == 's':
                        cript_arquivo_json.criptografar_arquivo()
                except ValueError as ve:
                    print(f"Erro: {ve}")
            elif escolha == '2':
                self.bd.listar_senhas()        
            elif escolha == '3':
                cript_arquivo_json.descriptografar_arquivo()
            elif escolha == '4':
                cript_arquivo_json.criptografar_arquivo()    
            elif escolha == 'q':
                print("Saindo...")
                break

            

    def menu(self):
        """Exibe as opções disponíveis para o usuário."""
        print("\n--- Gerenciador de Senhas CLI ---")
        print("1. Criar nova senha")
        print("2. Listar senhas")
        print("3. descriptografar arquivo ")
        print("4. Criptografar arquivo")
        print("Q. Sair")
        print("---------------------------------")    


    def criar_senha(self):
        self.controle.main()

            