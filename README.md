#  Genrok Case — Coletor de Leads

Este projeto foi desenvolvido como parte de um desafio técnico para demonstrar habilidades em desenvolvimento backend com **Python e Flask**.

O objetivo principal é criar uma API capaz de **receber e armazenar leads** provenientes de formulários, **notificar automaticamente** por email e Slack a cada novo cadastro, e permitir a **consulta dos leads registrados**.

---

##  Funcionalidades

- Recebe dados de formulários via requisição **POST**;
- Armazena informações em um banco de dados **SQLite3**;
- Envia notificações automáticas por **Email** e **Slack** sempre que um novo lead é cadastrado;
- Disponibiliza um endpoint para **listar todos os leads** cadastrados;
- Registra logs detalhados de eventos e erros da aplicação.

---

##  Tecnologias utilizadas

- **Python 3.13**
- **Flask** — framework web principal
- **SQLite3** — banco de dados leve e embutido
- **Flask-CORS** — permite comunicação entre domínios
- **smtplib** — envio de emails
- **requests** — integração com Slack via Webhook
- **logging** — registro de logs da aplicação

---

##  Estrutura do Projeto

Genrokcase/
│
├── app/
│ ├── init.py # Criação e configuração da aplicação Flask
│ ├── routes.py # Rotas da API (cadastrar e listar leads)
│ ├── db.py # Conexão e operações com o banco de dados SQLite
│ ├── notificacao.py # Envio de emails e notificações no Slack
│ └── logger.py # Configuração de logs da aplicação
│
├── run.py # Ponto de entrada para iniciar o servidor
├── requirements.txt # Dependências do projeto
└── README.md # Documentação


---

##  Como executar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/Bhaddad10/Genrokcase.git
cd Genrokcase
2. Crie um ambiente virtual


python -m venv venv
source venv/Scripts/activate  # Windows
3. Instale as dependências


pip install -r requirements.txt
4. Execute o servidor

python run.py
A aplicação ficará disponível em:

http://localhost:5000

🧩 Endpoints
🔹 Cadastrar novo lead
POST /recieve_leads

Exemplo de corpo (JSON):


{
  "nome": "João Silva",
  "telefone": "11999999999",
  "email": "joao@email.com",
  "assunto": "Interesse em consultoria"
}
Resposta (200):

{
  "mensagem": "Formulário recebido com sucesso!"
}
🔹 Listar todos os leads
GET /leads

Resposta (200):

[
  {
    "id": 1,
    "nome": "João Silva",
    "telefone": "11999999999",
    "email": "joao@email.com",
    "assunto": "Interesse em consultoria",
    "criado_em": "2025-10-28"
  }
]
 Notificações
A cada novo lead recebido:

Um email é enviado automaticamente com as informações do lead;

Uma notificação no Slack é disparada via Webhook informando o nome e o email do remetente.

Essas credenciais (SMTP e Webhook) são configuradas via variáveis de ambiente para manter segurança e evitar exposição de dados sensíveis no código.

 Logs
Todos os eventos importantes são registrados no arquivo de logs da aplicação, incluindo erros e ações de cadastro.

Exemplo de log:

2025-10-28 15:24:33 [INFO] Novo lead recebido: João Silva - joao@email.com
2025-10-28 15:24:33 [ERROR] Erro ao enviar notificação por e-mail: Timeout

Os logs ajudam a monitorar o comportamento da aplicação e facilitam o diagnóstico de problemas em ambiente de produção.

Arquitetura Geral

Formulário (Front-End)
        │
        ▼
Flask API  →  Banco de Dados SQLite
   │
   ├── Envio de Email (SMTP)
   └── Notificação Slack (Webhook)
A arquitetura é simples, modular e escalável, permitindo futuramente migrar para bancos como PostgreSQL ou adicionar filas de mensagens para notificações assíncronas.

Autor
Bruno Haddad
Desenvolvedor Python — Backend


Licença
Projeto desenvolvido exclusivamente para fins de avaliação técnica.