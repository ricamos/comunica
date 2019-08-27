#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

###Versão inicial 0.1	- Rio de Janeiro, 28 de maio de 2017
## Descrição inicial do progrma - Class para formas de comunicação, envio de relatorios e/ou avisos de sistemas de forma automatizada.

import smtplib
import sys

class Mail():

	#  remetente, destinatario, assunto, mensagem, anexo, servidor, username, senha):
	'''self.remetente = remetente
		self.destinatario = destinatario
		self.assunto = assunto
		self.mensagem = mensagem
		self.anexo = anexo
		self.servidor = servidor
		self.username = username
		self.senha = senha'''

	def __init__(self, servidor, port = 587):
		self.servidor = servidor
		self.port = port
		self.smtpObj = smtplib.SMTP(servidor, port) # Configura servidor
		
	def test_connection(self):	
		# Hello teste de conexão
		try:
			if self.smtpObj.ehlo()[0] == 250: 
				print("Requested mail action okay, completed")
		except:
			error = str (sys.exc_info()) 
			print (error)

	def mail_smtp_ttl(self):
		try:
			#smtpObj.ehlo()	# Hello teste de conexão
			smtpObj.starttls()
			smtpObj.login(self.username, self.senha)
			smtpObj.sendmail(self.remetente, self.destinatario, 'Subject:'+self.assunto+'\n'+self.mensagem)
			{}
			smtpObj.quit()
			
			print ("Mensagem eviada com sucesso!!!")
		
		except:
			error = str (sys.exc_info()[0]) 
			print("Deculpe! Alguma coisa deu errado ao tentar enviar email!")
			print (error)
			
			if error == "<class 'socket.gaierror'>" :
				print ("Verifique sua conexão com a internet e o endereço do servidor")
			
			if error == "<class 'smtplib.SMTPAuthenticationError'>" :
				print ("Verifique a senha. \nNo caso do Gmail verifique a opção Allow less apps")
	
