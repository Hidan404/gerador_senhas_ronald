from controllers.senha_controller import ExecutarControllers
from models.password_models import SenhaModel



class CliView():
    def __init__(self):
        self.controle = ExecutarControllers()
        self.senha_model = SenhaModel()

    def app(self):
        while