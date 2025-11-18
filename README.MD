Gerenciador de Senhas CLI
Um aplicativo de linha de comando para gerenciar senhas de forma segura, permitindo gerar, armazenar e criptografar senhas para diferentes sites e logins.

📋 Funcionalidades
Geração de Senhas Seguras: Cria senhas aleatórias com opções personalizáveis

Armazenamento Local: Salva senhas em arquivo JSON

Criptografia Avançada: Protege os dados com criptografia Fernet

Interface CLI Amigável: Menu interativo fácil de usar

Gestão de Múltiplas Contas: Armazena site, login e senha

🚀 Como Usar
Pré-requisitos
Python 3.6 ou superior

Dependências: cryptography

Instalação
bash
# Clone o repositório
git clone [url-do-repositorio]

# Instale as dependências
pip install cryptography
Execução
bash
python main.py
Menu Principal
Ao executar o programa, você verá as seguintes opções:

text
--- Gerenciador de Senhas CLI ---
1. Criar nova senha
2. Listar senhas
3. Descriptografar arquivo
4. Criptografar arquivo
Q. Sair
📝 Fluxo de Uso
Criar Nova Senha (Opção 1):

Digite o site (ex: google.com)

Digite o login/email

Defina o comprimento da senha

A senha será gerada automaticamente e salva no JSON

Opção de criptografar o arquivo imediatamente

Listar Senhas (Opção 2):

Exibe todas as senhas salvas

Mostra site, login e senha correspondente

Criptografia (Opções 3 e 4):

Criptografa o arquivo JSON para .enc

Descriptografa o arquivo .enc para JSON

Gerenciamento automático de chaves de criptografia

🏗️ Estrutura do Projeto
text
gerenciador-senhas/
│
├── main.py                          # Ponto de entrada da aplicação
├── models/
│   ├── criar_bd.py                  # Gerenciamento do banco de dados JSON
│   ├── password_models.py           # Modelo para geração de senhas
│   ├── site_login_models.py         # Modelo para sites e logins
│   └── criptografar_arquivo.py      # Criptografia de arquivos
├── controllers/
│   └── senha_controller.py          # Controlador principal
└── views/
    └── cli_view.py                  # Interface de linha de comando
🔧 Componentes Principais
Models
SenhaModel (password_models.py)
Gerencia a criação de senhas seguras com critérios personalizáveis.

Funcionalidades:

Geração de senhas usando secrets para segurança criptográfica

Configuração de comprimento e tipos de caracteres

Método from_prompt() para entrada interativa do usuário

Uso:

python
senha_model = SenhaModel()
senha_model.from_prompt()  # Solicita comprimento via input
senha_gerada = senha_model.gerar_senha()
SiteLoginModels (site_login_models.py)
Gerencia informações de sites e logins com registro temporal.

Funcionalidades:

Armazenamento de sites e logins com data/hora

Lista interna para gerenciamento de múltiplos registros

SenhasLoginsJson (criar_bd.py)
Combina funcionalidades de senhas e sites para persistência em JSON.

Funcionalidades:

Herda de SenhaModel e SiteLoginModels

Salva dados em arquivo JSON estruturado

Lista senhas salvas

Método salvar_json() para persistência completa

CriptArquivojson (criptografar_arquivo.py)
Gerencia criptografia e descriptografia de arquivos usando Fernet.

Funcionalidades:

Geração e armazenamento seguro de chaves

Criptografia de arquivos JSON para .enc

Descriptografia de arquivos .enc para JSON

Remoção segura de arquivos originais após criptografia

Controller
ExecutarControllers (senha_controller.py)
Orquestra a execução entre models e views.

Funcionalidades:

Coordena entrada do usuário (site, login)

Inicializa gerenciador de senhas

Executa fluxo principal de salvamento

View
CliView (cli_view.py)
Interface de linha de comando interativa.

Funcionalidades:

Menu principal com opções numeradas

Integração com todos os componentes

Fluxo de controle da aplicação

Tratamento de opções do usuário

🔒 Segurança
Implementações de Segurança
Criptografia Fernet: Usa biblioteca cryptography para proteção robusta

Gerenciamento Automático de Chaves: Gera e armazena chaves seguras em chave.key

Arquivos Protegidos: Define permissões restritas (600) em arquivos sensíveis

Geração Segura de Senhas: Utiliza módulo secrets em vez de random

Limpeza de Arquivos: Remove arquivos originais após criptografia bem-sucedida

Protocolo de Criptografia
python
# Geração de chave
chave = Fernet.generate_key()

# Criptografia
fernet = Fernet(chave)
criptografado = fernet.encrypt(conteudo)

# Descriptografia
conteudo = fernet.decrypt(arquivo_criptografado)
💾 Armazenamento de Dados
Estrutura do JSON
Os dados são salvos em senhas_logins.json com a estrutura:

json
{
    "registros": [
        {
            "site": "exemplo.com",
            "login": "usuario@email.com",
            "senha": "s3nh4-ger4d4"
        },
        {
            "site": "outrosite.com",
            "login": "meulogin",
            "senha": "0utr4-s3nh4"
        }
    ]
}
Fluxo de Dados
Entrada do Usuário → Site e login

Geração de Senha → Critérios personalizáveis

Persistência → Salva em JSON estruturado

Criptografia → Converte para arquivo .enc seguro

Recuperação → Descriptografa e lista quando necessário

⚠️ Observações Importantes
Segurança Crítica
Mantenha o arquivo chave.key em local seguro - sem ele não é possível descriptografar os dados

Faça backup da chave - perda da chave significa perda permanente dos dados criptografados

O arquivo JSON original é removido após criptografia para prevenir acesso não criptografado

Boas Práticas
Criptografe sempre após o uso para manter os dados protegidos

Use em ambiente seguro - evite computadores públicos ou compartilhados

Mantenha o software atualizado - especialmente a biblioteca cryptography

Limitações Conhecidas
Interface apenas em português

Dependência de arquivo local para armazenamento

Não possui sincronização em nuvem

🛠️ Desenvolvimento
Para Contribuir com o Projeto
Siga a estrutura MVC existente

Models: Lógica de negócio e dados

Views: Interface do usuário

Controllers: Orquestração entre models e views

Mantenha a separação de responsabilidades

Cada classe com propósito específico

Baixo acoplamento entre módulos

Adicione novas funcionalidades mantendo compatibilidade

Teste com fluxos existentes

Mantenha interface consistente

Estrutura de Arquivos Recomendada para Expansão
text
gerenciador-senhas/
│
├── main.py
├── requirements.txt
├── README.md
├── tests/                          # Para testes futuros
│   └── test_models.py
├── models/
│   ├── __init__.py
│   ├── criar_bd.py
│   ├── password_models.py
│   ├── site_login_models.py
│   └── criptografar_arquivo.py
├── controllers/
│   ├── __init__.py
│   └── senha_controller.py
└── views/
    ├── __init__.py
    └── cli_view.py
Possíveis Melhorias Futuras
Interface gráfica (GUI)

Sincronização com nuvem segura

Exportação/importação de dados

Geração de relatórios de segurança

Análise de força de senhas

Compartilhamento seguro de senhas

⚠️ AVISO LEGAL: Este é um projeto para fins educacionais. Use com responsabilidade e considere medidas de segurança adicionais para dados sensíveis. Os desenvolvedores não se responsabilizam por perda de dados ou violações de segurança.

