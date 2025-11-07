from datetime import datetime


class SiteLoginModels():
    login_lista = []

    def __init__(self, site,login):
        self.site = site
        self.login = login

    def salvar_na_lista(self):
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("Salvar endereço do site ou login")    
        try:
            escolha = input("Digite sua escolha SITE/LOGIN: ").lower()
            if escolha == "login":
                self.login_lista.append(f"{self.login} - Data: {data}")
            elif escolha == "site":
                self.login_lista.append(f"{self.site} - Data: {data}")     

        except Exception as e:
            print(f"Erro: {e}")    