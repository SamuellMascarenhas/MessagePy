# Automação de Envio de E-mails e Mensagens pelo WhatsApp

Este projeto tem como objetivo automatizar o envio de e-mails e mensagens pelo WhatsApp com base em dados extraídos de uma planilha Excel. O sistema é ideal para tarefas de comunicação em massa, como notificações ou campanhas, e é configurado para enviar e-mails e mensagens em dois estágios distintos.

## Visão Geral

1. *Leitura de Dados:* O sistema lê os dados de uma planilha Excel contendo informações de contato, incluindo e-mails e números de telefone.
2. *Envio de E-mails:* O sistema envia e-mails para todos os endereços listados na planilha.
3. *Envio de Mensagens pelo WhatsApp:* Após o envio dos e-mails, o sistema agenda o envio de mensagens pelo WhatsApp para os números listados na planilha.

## Requisitos

- *Python 3.x:* Certifique-se de ter o Python 3.x instalado em seu sistema.
- *Bibliotecas Python:*
  - pandas - Para manipulação e leitura de dados da planilha.
  - smtplib - Para envio de e-mails.
  - email - Para criação e formatação de e-mails.
  - pywhatkit - Para envio de mensagens pelo WhatsApp.
- *Planilha Excel (contatos.xlsx):* A planilha deve ter as seguintes colunas:
  - nome: Nome do contato (opcional).
  - telefone: Número de telefone para envio de mensagens pelo WhatsApp.
  - email: Endereço de e-mail para envio de mensagens.

## Desenvolvido por

Samuel Mascarenhas - [Portfolio](https://samuellmascarenhas.github.io/Portfolio/)
