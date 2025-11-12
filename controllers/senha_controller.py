from  models.criar_bd import SenhasLoginsJson


class ExecutarControllers(SenhasLoginsJson):
    def __init__(self, site=None, login=None):
        super().__init__(site, login)
        
    def main(self):
        # todo criar ordem de execução entre a logica e views
        pass    
