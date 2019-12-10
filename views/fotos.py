from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import threading as th
import numpy as np
import os, random

class Fotos(Frame):

	aspectratio = (960, 540)

	def __init__(self, master = None, bg = 'black', **kwargs):

		self.master = master
		self.color = bg
		super().__init__(self.master, kwargs, bg = self.color)
		# print(os.listdir('fotos'))
		self.pics = os.listdir('fotos')
		random.shuffle(self.pics)
		self.exibe()
		self.update()
		# print(self.pics)

	def exibe(self):

		self.imgcanvas = Label(self, bg = 'pink')
		self.imgcanvas.pack(side = 'right', fill = 'both', expand = True)

		self.imagemteste = ImageTk.PhotoImage(Image.open('fotos/'+self.pics.pop()).resize(self.aspectratio, Image.ANTIALIAS))
		# self.imagemteste = ImageTk.PhotoImage(Image.open('fotos/'+self.pics.pop()))
		self.imgcanvas.configure(image = self.imagemteste)

	def update(self):
		if self.pics:
			self.imagemteste = ImageTk.PhotoImage(Image.open('fotos/'+self.pics.pop()).resize(self.aspectratio, Image.ANTIALIAS))
			self.imgcanvas.configure(image = self.imagemteste)
		else:
			self.pics = os.listdir('fotos')
			random.shuffle(self.pics)
			self.imagemteste = ImageTk.PhotoImage(Image.open('fotos/'+self.pics.pop()).resize(self.aspectratio, Image.ANTIALIAS))
			self.imgcanvas.configure(image = self.imagemteste)

		self.after(10000, self.update)
