#SCRIPT APENAS PARA TESTES DE ENVIAR MENSAGEM NO WHATSAPP
import pywhatkit as kit
import datetime

numero = '+5531999999999'
mensagem = 'Mensagem de teste'
agora = datetime.datetime.now()
hora = agora.hour
minuto = agora.minute + 2  # enviar a mensagem em 2 minutos (tempo)

# Ajustar caso o minuto for maior que 59
if minuto > 59:
    minuto -= 60
    hora += 1

kit.sendwhatmsg(numero, mensagem, hora, minuto)
