#!/usr/bin/env python3
import json
import telebot,sys
from socket import timeout
import requests
import telebot,sys

BOT_TOKEN='telebot BOT_TOKEN'

services = [  \
				{ \
						 'nome': 'Name',\
						 'url' : 'http:', \
				}, \
				{ \
						 'nome': 'Name',\
						 'url' : 'http', \
						 'headers' : { 'Authorization' : 'xxxxxxxx' }, \
				}, \
				{ \
						 'nome': 'Name',\
						 'url' : 'http', \
						 'data' : json.dumps({ "key": "xxxxx", "other": "xxxx"}), \
						 'headers' : { 'Content-Type' : 'application/json'}, \
				}, \
				{ \
						 'nome': 'Name',\
						 'url' : 'http:', \
				}, \
  ]
response_timeout = 10           #in seconds

services = services[1:2]

for service in services:
	if not 'url' in service:
			continue
	print ('url:', service['url'])
	try:
		if 'data' in service:
			if 'headers' in service:
				response = requests.request("POST", url=service['url'], data=service['data'], headers=service['headers'], timeout=response_timeout)
			else:
				response = requests.request("POST", url=service['url'], data=service['data'], timeout=response_timeout)
			#print("certo", response.text)
			print(str(response.status_code) + ' ' + str(response.reason))
			if response.status_code != 200:
				tb = telebot.TeleBot(BOT_TOKEN)
				DESTINATION = xxxxx
				SUBJECT = service['nome']
				MESSAGE = 'status webservice ' + str(response.status_code)
				tb.send_message(DESTINATION,SUBJECT + '\n' + MESSAGE, disable_web_page_preview=True, parse_mode='HTML')

		else:
			if 'headers' in service:
				response = requests.request("GET", url=service['url'], headers=service['headers'], timeout=response_timeout )
			else:
				response = requests.request("GET", url=service['url'], timeout=response_timeout)
			if response.status_code != 200:
				tb = telebot.TeleBot(BOT_TOKEN)
				DESTINATION = xxxxx
				SUBJECT = service['nome']
				MESSAGE = 'status webservice ' + str(response.status_code)
				tb.send_message(DESTINATION,SUBJECT + '\n' + MESSAGE, disable_web_page_preview=True, parse_mode='HTML')
			else:
				print(str(response.status_code))
	except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
		tb = telebot.TeleBot(BOT_TOKEN)
		DESTINATION = xxxxx
		SUBJECT = service['nome']
		MESSAGE = 'Servico Indisponivel '
		tb.send_message(DESTINATION,SUBJECT + '\n' + MESSAGE, disable_web_page_preview=True, parse_mode='HTML')
	except Exception as e:
		print("Erro desconhecido para o servico:", service['url'])
		print (e)
