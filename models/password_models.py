import string
import random
import secrets


class PasswordModel():
    def __init__(self,maiusculas=True,minusculas=True):
        self.comprimento = int(input("Quantos caracteres: "))
        self.maiusculas = maiusculas
        self.minusculas = minusculas
        self.caracteres = list(string.ascii_letters)




senha = PasswordModel()
print(senha.caracteres)        
