from flask import Blueprint, request, jsonify
from app.db import insert_lead, get_all_leads, close_connection
from app.notificacao import notificar_novo_lead
from datetime import datetime
from app.logger import logger
from flask import render_template


bp = Blueprint('routes', __name__)

# Fecha conexão com o banco no final de cada request
@bp.teardown_app_request
def teardown_db(exception):
    close_connection(exception)

# Rota para cadastrar um novo lead, salva o lead e grava os logs
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

        logger.info(f"Novo Lead Recebido: {dados.get('nome')} - {dados.get('email')}")
        return jsonify({"status":"success","message":"Formulário recebido com sucesso!"}), 200
    except Exception as e:
        logger.error(f"Erro ao processar lead: {e}", exc_info=True)
        #print("Erro ao inserir lead:", e)
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
    

#rota para página web

@bp.route('/form')
def form():
    return render_template('form.html')
