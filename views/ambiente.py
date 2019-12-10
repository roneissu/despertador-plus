from tkinter import *
from tkinter import ttk, messagebox
import threading as th
import numpy as np

font = ("Calibri", 12, 'bold')


class Ambiente(Frame):

    def criaTemp(self):
        self.LabelTexto = Label(
            self, text='Temperatura ambiente: ', font=font, bg=self.color, fg="white")
        self.LabelTexto['font'] = 'Helvita 14'
        self.LabelTexto.grid(column=1, row=0, columnspan=2, sticky="NSWE")

        self.LabelTemp = Label(
            self, text='00.00°C', font=font, bg=self.color, fg="white")
        self.LabelTemp['font'] = 'Helvita 22 bold'
        self.LabelTemp.grid(column=3, row=0, columnspan=1, sticky="NSWE")

        self.oldtemp = 25.0

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(3, weight=1)
        
        self.after(1000, self.updateTemp)

    def updateTemp(self):
        add = (np.random.rand()-0.5)*2
        # print(add)
        newtemp = add+self.oldtemp
        self.oldtemp = newtemp
        self.LabelTemp.configure(text=f'{newtemp:.2f}°C')
        self.after(1000, self.updateTemp)

    def __init__(self, master=None, bg="black", **kwargs):
        self.master = master
        self.color = bg
        super().__init__(master, kwargs, bg=self.color)
        # self.__dummy__criabuts()

        self.criaTemp()
