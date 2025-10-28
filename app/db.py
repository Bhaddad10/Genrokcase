import os
import sqlite3
from flask import g

# Caminho do banco de dados na mesma pasta do projeto
current_folder = os.path.dirname(__file__)
DB_PATH = os.path.join(current_folder, "leads.db")

# Conexão com o banco de dados (mantida por request)
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
        db.row_factory = sqlite3.Row  # Para retornar dicionários
    return db

# Fecha conexão no fim da request
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Inicializa o banco e cria tabela se não existir
def init_db():
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            assunto TEXT NOT NULL,
            criado_em DATE DEFAULT (datetime('now','localtime'))
        )
    ''')
    db.commit()
    db.close()

# Insere novo lead
def insert_lead(nome, telefone, email, assunto):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO leads (nome, telefone, email, assunto)
        VALUES (?, ?, ?, ?)
    ''', (nome, telefone, email, assunto))
    db.commit()

# Consulta todos os leads
def get_all_leads():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM leads ORDER BY criado_em DESC")
    rows = cursor.fetchall()
    return [dict(row) for row in rows]
