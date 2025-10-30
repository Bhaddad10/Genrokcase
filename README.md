# Genrok Case — Coletor de Leads

Projeto desenvolvido como parte de desafios técnicos em **Python e Flask**.  

O objetivo do projeto é criar uma API capaz de:

- Receber e armazenar leads de formulários;
- Notificar automaticamente por **email** e **Slack** a cada novo cadastro;
- Permitir consulta dos leads registrados.

---

## Funcionalidades

- Recebe dados de formulários via requisição **POST**.  
- Armazena informações em **SQLite3**.  
- Envia notificações automáticas por **Email** e **Slack**.  
- Endpoint para listar todos os leads cadastrados.  
- Registro de logs detalhados para eventos e erros da aplicação.  

---

## Tecnologias utilizadas

- **Python 3.13**  
- **Flask** — framework web principal  
- **SQLite3** — banco de dados leve  
- **Flask-CORS** — permite comunicação entre domínios  
- **smtplib** — envio de emails  
- **requests** — integração com Slack via Webhook  
- **logging** — registro de logs da aplicação  

---

## Estrutura do Projeto

```
Genrokcase/
│
├── app/
│   ├── __init__.py        # Criação e configuração da aplicação Flask
│   ├── routes.py          # Rotas da API (cadastrar e listar leads)
│   ├── db.py              # Conexão e operações com o banco de dados SQLite
│   ├── notificacao.py     # Envio de emails e notificações no Slack
│   └── logger.py          # Configuração de logs da aplicação
│
├── run.py                 # Ponto de entrada para iniciar o servidor
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação
```

---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Bhaddad10/Genrokcase.git
cd Genrokcase
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o servidor

```bash
python run.py
```

A aplicação ficará disponível para testes em:

```
http://localhost:5000/form
```

---

## Endpoints

### Cadastrar novo lead

**POST** `/recieve_leads`  

Exemplo de corpo (JSON):

```json
{
  "nome": "João Silva",
  "telefone": "11999999999",
  "email": "joao@email.com",
  "assunto": "Interesse em consultoria"
}
```

Resposta (200):

```json
{
  "mensagem": "Formulário recebido com sucesso!"
}
```

### Listar todos os leads

**GET** `/leads`  

Resposta (200):

```json
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
```

---

## Notificações

A cada novo lead recebido:

- Um email é enviado automaticamente com as informações do lead;  
- Uma notificação no Slack é disparada via Webhook com nome e email do remetente.  

> As credenciais (SMTP e Webhook) são configuradas via variáveis de ambiente para manter a segurança e evitar exposição de dados sensíveis.

---

## Segurança

- Por motivos de segurança, as credenciais reais (senha de e-mail e URL do webhook Slack) não estão incluídas no repositório.
- Para o pleno funcionameto das notificações será necessário preencher as variaveis: *usuario*, *senha* (deve ser preenchida com uma variável ambiente por segurança), *webhook_url* (que também deve ser utilizada uma variável ambiente) e *destinatario*, todas no arquivo *notificacao.py*
- Sem o preenchimento destas variáveis, ainda será possivel o envio de leads e a captura de logs.

---

## Logs

Todos os eventos importantes são registrados no arquivo de logs da aplicação, incluindo erros e ações de cadastro.

Exemplo:

```
2025-10-28 15:24:33 [INFO] Novo lead recebido: João Silva - joao@email.com
2025-10-28 15:24:33 [ERROR] Erro ao enviar notificação por e-mail: Timeout
```

---

## Arquitetura Geral

```
Formulário (Front-End)
        │
        ▼
   Flask API  →  Banco de Dados SQLite
       │
       ├── Envio de Email (SMTP)
       └── Notificação Slack (Webhook)
```

Arquitetura modular, simples e escalável, permitindo:

- Migração para bancos como PostgreSQL;  
- Adição de filas de mensagens para notificações assíncronas.

---

## Autor

**Bruno Haddad**  
Desenvolvedor Python — Backend  
---

## Licença

Projeto desenvolvido exclusivamente para fins de avaliação técnica.
