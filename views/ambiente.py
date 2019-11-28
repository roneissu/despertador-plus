from tkinter import *
from tkinter import ttk, messagebox
import threading as th
import numpy as np

font = ("Calibri", 12, 'bold')


class Ambiente(Frame):

    def criaTemp(self):

        self.LabelTexto = Label(
            self, text='Temperatura ambiente: ', font=font, bg=self.color)
        self.LabelTemp = Label(self, text='0°C', font=font, bg=self.color)
        self.LabelTemp.config(anchor='center')

        self.LabelTexto.grid(column=0, row=0, columnspan=1, sticky='nsew')
        self.LabelTemp.grid(column=1, row=0, columnspan=1, sticky='nsew')
        self.oldtemp = 25.0

        for i in range(self.grid_size()[0])[0:]:
            self.columnconfigure(i, weight=1)

        self.after(1000, self.updateTemp)

    def updateTemp(self):
        add = (np.random.rand()-0.5)*2
        # print(add)
        newtemp = add+self.oldtemp
        self.oldtemp = newtemp
        self.LabelTemp.configure(text=f'{newtemp:.2f}°C')
        self.after(1000, self.updateTemp)

    def __init__(self, master=None, bg='light blue', **kargs):

        self.master = master
        self.color = bg

        super().__init__(master, bg=self.color, **kargs)
        # self.__dummy__criabuts()
        self.criaTemp()
