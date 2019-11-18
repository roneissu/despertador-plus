from tkinter import *
from tkinter import ttk, messagebox
import threading as th 
import numpy as np 


class Ambiente(Frame):
	
	font = ("Calibri", 12, 'bold')

	def __init__(self, master = None, bg = 'light blue', **kargs):

		self.master = master
		self.color = bg

		super().__init__(master, bg = self.color, **kargs)
		# self.__dummy__criabuts()
		self.criaTemp()


	def criaTemp(self):

		self.LabelTexto = Label(self, text = 'Temperatura ambiente: ', font = self.font, bg = self.color)
		self.LabelTemp = Label(self, text = '0°C', font = self.font, bg = self.color)
		self.LabelTemp.config(anchor = 'center')
		self.columnconfigure(0, weight = 1)
		self.columnconfigure(1, weight = 1)
		
		self.LabelTexto.grid(column = 0, row = 0, columnspan = 1, sticky = 'nsew')
		self.LabelTemp.grid(column = 1, row = 0, columnspan = 1, sticky = 'nsew')
		
		self.oldtemp = 25.0
		self.after(1000, self.updateTemp)
		
	def updateTemp(self):
		add = (np.random.rand()-0.5)*2
		print(add)
		newtemp = add+self.oldtemp
		self.oldtemp = newtemp
		self.LabelTemp.configure(text = f'{newtemp:.2f}°C')
		self.after(1000, self.updateTemp)





	def __dummy__criabuts(self):

		but1 = Button(self, text = 'Hello')
		but1.grid(column = 0, row = 0, columnspan = 2, sticky= 'nsew')
		but2 = Button(self, text = 'world')
		but2.grid(column = 1, row = 1, columnspan = 4, sticky= 'nsew')

		self.columnconfigure(0, weight = 1)
		self.columnconfigure(1, weight = 1)
		self.columnconfigure(2, weight = 1)