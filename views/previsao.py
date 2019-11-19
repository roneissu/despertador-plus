from tkinter import *
from tkinter import ttk, messagebox
import numpy as np 
import requests





class Previsao(Frame):
    
    font = ('Calibri', 12, 'bold')

    city = 'Belo Horizonte'
	previs_addr='http://api.openweathermap.org/data/2.5/forecast?appid=0c42f7f6b53b244c78a418f4f181282a&q='
	previs_addr='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
	previs_url = previs_addr + city + '&units=metric'

	dia_url = dia_addr + city + '&units=metric'



    def __init__(self, master = None, bg = 'light blue', *kargs):

    	self.master = master
    	self.color = bg
    	super()__init__(master, bg, *kargs)

    def get_prev(self):

    	dados_prev = requests.get(previs_url).json()
		dados_dia = requests.get(dia_url).json()
