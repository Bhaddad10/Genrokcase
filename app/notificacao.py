import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from app.logger import logger

#função que formata os textos das notificações
def formatar_textos(lead):

    nome = lead.get('nome', 'N/A')
    email = lead.get('email', 'N/A')
    telefone = lead.get('telefone', 'N/A')
    assunto = lead.get('assunto', 'N/A')
    criado_em = lead.get('criado_em', 'N/A')

    # Texto e-mail
    texto_email = f"""
        Um novo lead foi enviado:

        Nome: {nome}
        Email: {email}
        Telefone: {telefone}
        Assunto: {assunto}
        Data: {criado_em}
        """

    # Texto Slack
    texto_slack = f"""
        *Novo Lead Recebido!*
        *Nome:* {nome}
        *Email:* {email}
        *Telefone:* {telefone}
        *Assunto:* {assunto}
        *Data:* {criado_em}
        """

    return texto_email.strip(), texto_slack.strip()

#envia email com as informações do lead
def enviar_email(destinatario, assunto, mensagem):
  
    #Envia e-mail usando SMTP do Gmail.
 
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    usuario = "haddad.bruno00@gmail.com"#Email de qual voce deve criar uma senha de app para desparar os emails
    senha = ""  #senha de app deve ficar salva como variavel ambiente, gerada nas configurações de conta
    #senha = os.getenv("GOOGLE_PASSWORD")

    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(usuario, senha)
        server.send_message(msg)
        server.quit()
        logger.info(f"Email enviado para: {destinatario}")
        print("E-mail enviado com sucesso!")
    except Exception as e:
        logger.error(f"Erro ao enviar email: {e}", exc_info=True)
        print("Erro ao enviar:", e)

#envia notificação para o slack com informações do lead
def enviar_slack(mensagem):

    webhook_url = ""#Por segurança o url webhook deve ficar salva como variavel ambiente, link gerado a partir do app criado no slack
     #webhook_url = os.getenv("SLACK_WEBHOOK")
    if not webhook_url:
        print("Webhook não encontrado!")
        return

    payload = {"text": mensagem}

    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            logger.info(f"Notificação enviada para slack")
            print("Notificação enviada para o Slack!")
        else:
            logger.error(f"Falha ao enviar para Slack: {response.status_code} - {response.text}")
            print(f"Falha ao enviar: {response.status_code}, {response.text}")
    except Exception as e:
        logger.error(f"Erro ao enviar notificação para Slack: {e}", exc_info=True)
        print("Erro ao enviar:", e)


def notificar_novo_lead(lead):
    #formata as notificações

    texto_email, texto_slack = formatar_textos(lead)

    # Envia e-mail
    enviar_email(
        destinatario="haddad.bruno00@gmail.com",
        assunto=f"Novo lead: {lead.get('nome','N/A')}",
        mensagem=texto_email
    )

    # Envia Slack
    enviar_slack(texto_slack)
