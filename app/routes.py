from flask import Blueprint, request, jsonify
from .db import insert_lead, get_all_leads, close_connection
from .notificacao import notificar_novo_lead
from datetime import datetime

bp = Blueprint('routes', __name__)

# Fecha conexão com o banco no final de cada request
@bp.teardown_app_request
def teardown_db(exception):
    close_connection(exception)

# Rota para cadastrar um novo lead
@bp.route('/recieve_leads', methods=['POST'])
def receber_lead():
    dados = request.get_json()
    try:
        insert_lead(
            dados['nome'],
            dados['telefone'],
            dados['email'],
            dados['assunto']
        )
        notificar_novo_lead({
            'nome': dados['nome'],
            'telefone': dados['telefone'],
            'email': dados['email'],
            'assunto': dados['assunto'],
            'criado_em': datetime.now().strftime("%d/%m/%Y")
        })

        return jsonify({'mensagem': 'Formulário recebido com sucesso!'}), 200
    except Exception as e:
        print("Erro ao inserir lead:", e)
        return jsonify({'erro': 'Ocorreu um erro ao salvar o lead'}), 500

# Rota para listar todos os leads
@bp.route('/leads', methods=['GET'])
def listar_leads():
    try:
        leads = get_all_leads()
        return jsonify(leads), 200
    except Exception as e:
        print("Erro ao listar leads:", e)
        return jsonify({'erro': 'Ocorreu um erro ao listar os leads'}), 500
