import string
import secrets


class SenhaModel():
    def __init__(self,maiusculas=True,minusculas=True,simbolos=True,digitos=True):
        self.comprimento = int(input("Quantos caracteres: "))
        self.maiusculas = maiusculas
        self.minusculas = minusculas
        self.digitos = digitos
        self.simbolos = simbolos
        self.caracteres = list(string.ascii_letters)
        self.senhas_geradas = []

    def gerar_senha(self):
        
        while True:
            try:
                if self.maiusculas:
                    self.caracteres.extend(string.ascii_uppercase)
                if self.minusculas:
                    self.caracteres.extend(string.ascii_lowercase)
                if self.simbolos:
                    self.caracteres.extend(string.punctuation)   
                if self.digitos:
                    self.caracteres.extend(string.digits)    
                else:
                    self.caracteres

                self.senhas_geradas.append("".join([secrets.choice(self.caracteres) for _ in range(self.comprimento)]))   
                print(self.senhas_geradas) 

                return self.senhas_geradas
                
            except Exception as e:
                pass





senha = SenhaModel()
print(senha.gerar_senha())        
