import string
import secrets
from typing import Optional

class SenhaModel():
    def __init__(self, comprimento: Optional[int] = None,
                 maiusculas=True, minusculas=True, simbolos=True, digitos=True):
        """
        Se comprimento for None, não pede input — isso evita prompts ao instanciar.
        Use `from_prompt()` para criar a partir de input.
        """
        '''
        erros
        '''
        self.comprimento = comprimento
        self.maiusculas = maiusculas
        self.minusculas = minusculas
        self.digitos = digitos
        self.simbolos = simbolos
        self.caracteres = list(string.ascii_letters)
        self.senhas_geradas = []


    def from_prompt(self):
        self.comprimento = int(input("Quantos caracteres: "))
        return self.comprimento
        

    def gerar_senha(self):
        if self.comprimento is None:
            raise ValueError("Comprimento da senha não definido hahaha")
        # monta charset
        charset = []
        if self.maiusculas:
            charset.extend(string.ascii_uppercase)
        if self.minusculas:
            charset.extend(string.ascii_lowercase)
        if self.simbolos:
            charset.extend(string.punctuation)
        if self.digitos:
            charset.extend(string.digits)
        # gera
        print(type(self.comprimento))
        senha = "".join(secrets.choice(charset) for _ in range(self.comprimento))
        self.senhas_geradas.append(senha)
        return senha




      
