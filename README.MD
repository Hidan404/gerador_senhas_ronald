# 🔐 Gerenciador de Senhas CLI

Um aplicativo de linha de comando para gerenciar senhas de forma segura, permitindo gerar, armazenar e criptografar senhas para diferentes sites e logins.

---

## 📋 Funcionalidades

- **Geração de Senhas Seguras:** Cria senhas aleatórias com opções personalizáveis  
- **Armazenamento Local:** Salva senhas em arquivo JSON  
- **Criptografia Avançada:** Protege os dados com criptografia **Fernet**  
- **Interface CLI Amigável:** Menu interativo fácil de usar  
- **Gestão de Múltiplas Contas:** Armazena site, login e senha  

---

## 🚀 Como Usar

### ✔️ Pré-requisitos
- Python **3.6+**
- Dependência: `cryptography`

### 📦 Instalação

```bash
# Clone o repositório
git clone [url-do-repositorio]

# Instale as dependências
pip install cryptography
▶️ Execução
bash
Copiar código
python main.py
🧭 Menu Principal
markdown
Copiar código
--- Gerenciador de Senhas CLI ---
1. Criar nova senha
2. Listar senhas
3. Descriptografar arquivo
4. Criptografar arquivo
Q. Sair
📝 Fluxo de Uso
🔑 1. Criar Nova Senha
Digite o site (ex: google.com)

Digite o login/e-mail

Defina o comprimento da senha

A senha é gerada automaticamente e salva no JSON

Pode criptografar o arquivo imediatamente

📄 2. Listar Senhas
Exibe todas as senhas salvas

Mostra site, login e senha correspondente

🔐 3 e 4. Criptografia
Criptografa o arquivo JSON → .enc

Descriptografa .enc → JSON

Gera e gerencia chaves automaticamente

🏗️ Estrutura do Projeto
bash
Copiar código
gerenciador-senhas/
│
├── main.py                          # Ponto de entrada
├── models/
│   ├── criar_bd.py                  # Gerencia o "banco" JSON
│   ├── password_models.py           # Modelo de criação de senhas
│   ├── site_login_models.py         # Modelo para sites e logins
│   └── criptografar_arquivo.py      # Criptografia de arquivos
├── controllers/
│   └── senha_controller.py          # Controlador principal
└── views/
    └── cli_view.py                  # Interface CLI
🔧 Componentes Principais
🧩 Models
SenhaModel (password_models.py)
Gera senhas seguras usando secrets

Personalização de comprimento e caracteres

Método from_prompt() para solicitar dados ao usuário

SiteLoginModels (site_login_models.py)
Armazena sites e logins com registro de data/hora

SenhasLoginsJson (criar_bd.py)
Herda de outros models

Salva dados no JSON

Lista registros existentes

CriptArquivojson (criptografar_arquivo.py)
Usa Fernet para criptografar/descriptografar

Gera chave e salva em chave.key

Remove arquivos originais após criptografia

🕹️ Controller
ExecutarControllers (senha_controller.py)
Coordena fluxo entre models e views

Solicita informações do usuário

Executa todo o processo de salvamento de senha

🎛️ View
CliView (cli_view.py)
Exibe o menu principal

Recebe opções do usuário

Chama os controladores necessários

🔒 Segurança
Implementações
Criptografia Fernet

Arquivo chave.key gerado automaticamente

Permissões restritas (600)

Uso de secrets em vez de random

Remoção automática de JSON original após criptografia

Exemplo de Criptografia
python
Copiar código
chave = Fernet.generate_key()
fernet = Fernet(chave)
criptografado = fernet.encrypt(conteudo)
conteudo = fernet.decrypt(arquivo_criptografado)
💾 Armazenamento de Dados
Estrutura do JSON
json
Copiar código
{
    "registros": [
        {
            "site": "exemplo.com",
            "login": "usuario@email.com",
            "senha": "s3nh4-ger4d4"
        }
    ]
}
Fluxo de Dados
Usuário → Geração de Senha → JSON → Criptografia → Descriptografia (quando necessário)

⚠️ Observações Importantes
Segurança Crítica
Nunca perca o arquivo chave.key

Sem ele, não há como recuperar os dados

Faça backup da chave em local seguro

Boas Práticas
Criptografe sempre após uso

Evite usar em computadores públicos

Mantenha cryptography atualizada

Limitações
Sem interface gráfica

Sem sincronização em nuvem

Apenas em português

🛠️ Desenvolvimento
Estrutura Sugerida para Expansão
css
Copiar código
gerenciador-senhas/
├── main.py
├── requirements.txt
├── README.md
├── tests/
│   └── test_models.py
├── models/
├── controllers/
└── views/
Possíveis Melhorias Futuras
Interface gráfica (GUI)

Sincronização com nuvem

Exportação/importação de dados

Relatórios de segurança

Testes automatizados

⚠️ AVISO LEGAL
Este projeto é para fins educacionais. Use com responsabilidade.
Os desenvolvedores não se responsabilizam por perda de dados ou falhas de segurança.
