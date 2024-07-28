import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pywhatkit as kit
import time

# Configurações do IMAP (para leitura de e-mails)
email_de = 'seuemail@email.com'
senha = 'sua_senha'
servidor_imap = 'mail.servidor'   
porta_imap = 993  # Porta padrão para IMAP sobre SSL

# Configurações do SMTP (para envio de e-mails)
servidor_smtp = 'mail.servidor'
porta_smtp = 587  # Porta padrão para SMTP com TLS

# Dados para envio
assunto = 'Assunto do Email'
corpo = 'Mensagem padrão para e-mail.'
mensagem_whatsapp = 'Mensagem padrão para WhatsApp.'

# Função para enviar e-mail
def enviar_email(email_para, assunto, corpo):
    try:
        msg = MIMEMultipart()
        msg['From'] = email_de
        msg['To'] = email_para
        msg['Subject'] = assunto
        msg.attach(MIMEText(corpo, 'plain'))
        with smtplib.SMTP(servidor_smtp, porta_smtp) as servidor:
            servidor.starttls()
            servidor.login(email_de, senha)
            servidor.send_message(msg)
        print(f"Email enviado para {email_para}")
    except Exception as e:
        print(f"Falha ao enviar e-mail para {email_para}. Erro: {e}")

# Função para enviar mensagens pelo WhatsApp usando pywhatkit 
def enviar_whatsapp(numero, mensagem):
    try:
        hora_atual = time.localtime()
        hora = hora_atual.tm_hour
        minuto = hora_atual.tm_min + 2  # Adiciona 2 minutos para garantir tempo suficiente

        # Enviar mensagem usando pywhatkit
        kit.sendwhatmsg(f"+{numero}", mensagem, hora, minuto)
        print(f"Mensagem agendada para {numero} às {hora}:{minuto}")
        time.sleep(20)  # Espera para garantir que a mensagem seja enviada
    except Exception as e:
        print(f"Falha ao enviar mensagem para {numero}. Erro: {e}")

# Leitura da planilha
arquivo_excel = 'contatos.xlsx'
df = pd.read_excel(arquivo_excel)

# Verifique o nome das colunas na planilha
print("Nomes das colunas:", df.columns.tolist())

# Remover linhas onde telefone ou e-mail são NaN
df = df.dropna(subset=['telefone', 'email'])

# Verifique os dados carregados
print("Dados carregados:")
print(df)

# Separar telefones e e-mails
telefones = df['telefone'].astype(str).tolist()
emails = df['email'].tolist()

# Envio de e-mails
print(f"Total de e-mails para enviar: {len(emails)}")
for email in emails:
    if pd.notna(email):  # Verifique se o email não é NaN
        enviar_email(email, assunto, corpo)

# Espera para garantir que todos os e-mails sejam enviados
print("Pausa para garantir o envio dos e-mails...")
time.sleep(60)

# Envio de mensagens via WhatsApp
print(f"Total de telefones para enviar: {len(telefones)}")
for telefone in telefones:
    if pd.notna(telefone):  # Verifique se o telefone não é NaN
        enviar_whatsapp(telefone, mensagem_whatsapp)

print("Envio concluído.")
