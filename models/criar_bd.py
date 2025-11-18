import json
from datetime import datetime
from pathlib import Path
from .password_models import SenhaModel
from .site_login_models import SiteLoginModels


class SenhasLoginsJson(SenhaModel, SiteLoginModels):
    def __init__(self, site=None, login=None):
        super().__init__()
        SiteLoginModels.__init__(self, site, login)
        self.caminho = Path(__file__).resolve().parent
        self.nome_caminho = "senhas_logins.json"

    def caminho_json(self):
        return self.caminho / self.nome_caminho

    def salvar_json(self):

        self.from_prompt()
        
        arquivo = self.caminho_json()
        

        # Gera a senha
        senha_gerada = self.gerar_senha()

        novo_registro = {
            "site": self.site,
            "login": self.login,
            "senha": senha_gerada,
        }

        if not arquivo.exists():
            dados = {"registros": [novo_registro]}
        else:
            with open(arquivo, "r", encoding="utf-8") as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    dados = {"registros": []}

            dados["registros"].append(novo_registro)

        # Salva no JSON
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

        print(f"✅ Dados salvos com sucesso em: {arquivo}")

        return arquivo
    
    def listar_senhas(self):
        arquivo = self.caminho_json()
        if not arquivo.exists():
            print("Nenhum registro encontrado.")
            return

        with open(arquivo, "r", encoding="utf-8") as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                print("Nenhum registro encontrado.")
                return

        print("\n--- Senhas Salvas ---")
        for registro in dados.get("registros", []):
            print(f"Site: {registro['site']}")
            print(f"Login: {registro['login']}")
            print(f"Senha: {registro['senha']}")
            print("---------------------")


'''
if __name__ == "__main__":
    site = input("Digite o site: ")
    login = input("Digite o login: ")

    gerenciador = SenhasLoginsJson(site, login)
    gerenciador.salvar_json()

'''   