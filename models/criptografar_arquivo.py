from cryptography.fernet import Fernet
from pathlib import Path
import os

class CriptArquivojson:
    def __init__(self, base_dir: Path = None):
        self.chave = "chave.key"
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).resolve().parent
        self.dados_criptografado = self.base_dir / "senhas_logins.json.enc"
        self.nome_json = self.base_dir / "senhas_logins.json"  # caminho direto sem instanciar os objetos lembrar desse comentario

    def caminho_chave(self) -> Path:
        return self.base_dir / self.chave

    def remover_arquivoCriptografado(self):
        return os.remove(self.dados_criptografado)
    
    def remover_arquivo_json(self):
        return os.remove(self.nome_json)

    def gerar_chave(self):
        key_file = self.caminho_chave()
        if key_file.exists():
            print("Chave já existe em:", key_file)
            return key_file.read_bytes()
        chave = Fernet.generate_key()
        key_file.write_bytes(chave)
        try:
            key_file.chmod(0o600)
        except Exception:
            pass
        print("Chave gerada e salva em:", key_file)
        return chave

    def carregar_arquivo_senhas(self) -> Path:
        # Retorna o caminho direto, sem instanciar outras classes que pedem input
        return self.nome_json

    def criptografar_arquivo(self):
        json_path = self.carregar_arquivo_senhas()
        if not json_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {json_path}")

        key_path = self.caminho_chave()
        if not key_path.exists():
            print("Chave não encontrada. Gerando nova chave...")
            self.gerar_chave()

        chave = key_path.read_bytes()
        fernet = Fernet(chave)

        # Lê conteúdo do JSON (bytes)
        le_conteudo = json_path.read_bytes()

        # Criptografa
        criptografado = fernet.encrypt(le_conteudo)

        # Escrevendoo arquivo .enc
        # Dando permissão padrão
        self.dados_criptografado.write_bytes(criptografado)
        try:
            self.dados_criptografado.chmod(0o600)
        except Exception:
            pass

        # Remover o arquivo original somente após sucesso
        # (fazer backup se quiser)
        #json_path.unlink()
        self.remover_arquivo_json()
        print("Arquivo criptografado salvo em:", self.dados_criptografado)

    def descriptografar_arquivo(self):
        enc_path = self.dados_criptografado
        if not enc_path.exists():
            raise FileNotFoundError(f"Arquivo criptografado não encontrado: {enc_path}")
        chave = self.caminho_chave().read_bytes()
        fernet = Fernet(chave)
        conteudo = fernet.decrypt(enc_path.read_bytes())
        # salva com mesmo nome sem .enc
        out_path = enc_path.with_suffix("")  # remove .enc
        out_path.write_bytes(conteudo)
        self.remover_arquivoCriptografado()
        print("Arquivo descriptografado salvo em:", out_path)



