from comunica import Mail 

remetente = "ricardo.rcj@gmail.com"
destinatario = "ricardo.rcj@gmail.com"
assunto = "Teste de email"
mensagem = "Teste de envio de email"
anexo = ""
servidor = "smtp.gmail.com"
username = "ricardo.rcj@gmail.com"
senha = "S@muelC0e1hoS4"

config =Mail(remetente, destinatario, assunto, mensagem, anexo, servidor, username, senha)

config.mail_smtp_ttl()

"""
Ref:
https://realpython.com/python-send-email/
https://realpython.com/lessons/connecting-mail-server-smtplib/


Projeto:

Configurar o servidor separadamente
enviar email com minimo de variaveis
criar metodos de anexar arquivo e outras funções
esconder a senha no escript
"""