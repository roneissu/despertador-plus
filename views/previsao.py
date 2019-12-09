from tkinter import *
from tkinter import ttk, messagebox
import numpy as np 
import requests, time
import pprint as pp 





class Previsao(Frame):
	
	font = ('Calibri', 12, 'bold')

	city = 'Belo Horizonte'
	previs_addr='http://api.openweathermap.org/data/2.5/forecast?appid=0c42f7f6b53b244c78a418f4f181282a&q='
	dia_addr='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
	
	previs_url = previs_addr + city + '&units=metric&lang=pt'
	dia_url = dia_addr + city + '&units=metric&lang=pt'



	def __init__(self, master = None, bg = 'light blue', **kargs):

		self.master = master
		self.color = bg
		super().__init__(master, bg = bg, **kargs)
		
		try: 
			self.getDia()
			self.getPrev()
			pp.pprint(self.previsao[3])
			self.convData(self.previsao[3])
			self.makeCards()

		except Exception as e:
			# Colocar tela de "sem conexão"
			print(e)
			pass


	def makeCards(self):

		self.cards = []

		for i in self.previsao:
			self.cards.append(prevSingle(self, bg = self.color, forecast = i, bd = 4, relief = 'raised'))

		# maxw = max(self.cards, key = lambda x : x.card.winfo_width())
		n = 0
		for i in self.cards:
			# i.configure(width = maxw)
			i.grid(row = n, pady = (5, 0), sticky="NSWE")
			n+=1

		# print(self.grid_size())

		for i in range(self.grid_size()[1]):
			self.rowconfigure(i, weight = 1)
		self.columnconfigure(0, weight = 1)
		

	def getPrev(self):

		dados_prev = requests.get(self.previs_url).json()
		# dados_dia = requests.get(dia_url).json()

		# pp.pprint(dados_prev)

		dados = dados_prev['list'][0]
		dataold = dados['dt']
		diaold = dados['dt_txt'].split()[0]
		offset = dados_prev['city']['timezone']
		dias = []
		infodia = {}
		cnt = 1
		temp = dados['main']['temp']
		tempmin = dados['main']['temp_min']
		tempmax = dados['main']['temp_max']
		clima = [dados['weather'][0]['description']]

		for i in dados_prev['list'][1:]:
			datanew = i['dt']
			dianew = i['dt_txt'].split()[0]
			if dianew !=  diaold:
				infodia['dia'] = dataold 
				infodia['timezone'] = offset
				infodia['num'] = cnt
				infodia['temp'] = round(temp/max(cnt, 1), 2)
				infodia['temp_min'] = round(tempmin/max(cnt, 1), 2)
				infodia['temp_max'] = round(tempmax/max(cnt, 1), 2)
				infodia['clima'] = max(clima, key = clima.count)
				dias.append(infodia)
				infodia = {}
				temp = 0
				tempmin = 0
				tempmax = 0
				cnt = 0
				clima = []
				diaold = dianew
				dataold = datanew

			cnt+=1
			temp += i['main']['temp']
			tempmin += i['main']['temp_min']
			tempmax += i['main']['temp_max']
			clima.append(i['weather'][0]['description'])


		infodia['dia'] = dataold
		infodia['timezone'] = offset
		infodia['num'] = cnt
		infodia['temp'] = round(temp/max(cnt, 1), 2)
		infodia['temp_min'] = round(tempmin/max(cnt, 1), 2)
		infodia['temp_max'] = round(tempmax/max(cnt, 1), 2)
		infodia['clima'] = max(clima, key = clima.count)
		dias.append(infodia)

		self.previsao = dias
		# pp.pprint(self.previsao)

	def getDia(self):

		dados_dia = requests.get(self.dia_url).json()

		self.dia = {
			'dia' 			: dados_dia['dt'],
			'timezone' 		: dados_dia['timezone'],
			'temperatura' 	: dados_dia['main']['temp'],
			'temp_min' 		: dados_dia['main']['temp_min'],
			'temp_max' 		: dados_dia['main']['temp_max'],
			'clima' 		: dados_dia['weather'][0]['description']
		}

	def convData(self, struct):

		meses = [
			'Janeiro',
			'Fevereiro',
			'Março',
			'Abril',
			'Maio',
			'Junho',
			'Julho',
			'Agosto',
			'Setembro',
			'Outubro',
			'Novembro',
			'Dezembro'
		]




		epoch_s = struct['dia'] + struct['timezone']
		dados = time.gmtime(epoch_s)

		returns = {
			'data_txt' 	: f'{dados.tm_mday} de {meses[dados.tm_mon-1]} de {dados.tm_year}',
			'data' 		: f'{dados.tm_mday}-{dados.tm_mon}-{dados.tm_year}',
			'hora' 		: f'{dados.tm_hour}:{str(dados.tm_min).zfill(2)}'
		}

		pp.pprint(returns)

		return returns



class prevSingle(Frame):

	font = ('Calibri', 12, 'bold')
	fontbig = ('Calibri', 18, 'bold')
	fonthuge = ('Calibri', 24, 'bold')

	def __init__(self, master = None, bg = 'light blue', forecast = None, **kargs):
		self.master = master
		self.color = bg
		super().__init__(master, bg = bg, **kargs)
		self.forecast = forecast
		self.genFrame()




	def genFrame(self):

		self.card = Frame(self, bg = self.color)

		# icon = Canvas(self.card, width = 50, height = 50, bd = 4, relief = 'sunken')
		icon = Canvas(self.card, width = 50, height = 50)
		icon.grid(column = 0, row = 0, rowspan = 4)

		clima = Label(self.card, text = self.forecast['clima'], width = 25, font = self.font, bg = self.color, anchor = 'center')
		clima.grid(column = 0, row = 4, sticky = 'nswe')

		temp = Label(self.card, text = str(self.forecast['temp'])+'°C', font = self.fonthuge, bg = self.color, anchor = 'center')
		temp.grid(column = 1, row = 0, rowspan = 5, sticky = 'nswe')

		tempmax = Label(self.card, text = str(self.forecast['temp_max'])+'°C', font = self.fontbig, bg = self.color, anchor = 'center')
		tempmax.grid(column = 2, row = 0, rowspan = 2, sticky = 'nswe')

		tempmin = Label(self.card, text = str(self.forecast['temp_min'])+'°C', font = self.fontbig, bg = self.color, anchor = 'center')
		tempmin.grid(column = 2, row = 3, rowspan = 2, sticky = 'nswe')


		print(self.card.grid_size())
		for i in range(self.card.grid_size()[1]):
			self.card.rowconfigure(i, weight = 1)

		for i in range(self.card.grid_size()[0]):
			self.card.columnconfigure(i, weight = 1)


		self.card.pack(fill = 'both', expand = 1)

		
