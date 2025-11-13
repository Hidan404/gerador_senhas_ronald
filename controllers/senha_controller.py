from  models.criar_bd import SenhasLoginsJson


class ExecutarControllers():

    def main(self):
        # todo criar ordem de execução entre a logica e views
        site = input("Digite seu site: ") 
        login = input("Digite o login: ")
        
        gerenciador = SenhasLoginsJson(site, login)
        gerenciador.salvar_json()
        
