from comunica import Mail 

remetente = "remetente@gmail.com"
destinatario = "destino@gmail.com"
assunto = "Teste de email"
mensagem = "Teste de envio de email"
anexo = ""
servidor = "smtp.gmail.com"
username = "user@gmail.com"
senha = "xxxxxxx"

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
