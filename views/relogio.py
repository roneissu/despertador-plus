from datetime import datetime
from time import strftime
from tkinter import *


class Relogio(Frame):
    def troca(self):
        self.hora['text'] = strftime('%H:')
        self.minuto['text'] = strftime('%M')
        self.segundo['text'] = strftime('%S')

        self.after(100, self.troca)

    def __init__(self, master=None, bg=""):
        self.master = master
        super().__init__(master)

        self.posX = 0.08
        self.posY = 0.15

        self.hora = Label()
        self.hora.place(relx=self.posX, rely=self.posY)
        self.hora['text'] = strftime('%H:')
        self.hora['font'] = 'Helvita 100 bold'
        self.hora.config(bg=bg, highlightthickness=0, borderwidth=0)

        self.minuto = Label()
        self.minuto.place(relx=self.posX+0.18, rely=self.posY)
        self.minuto['text'] = strftime('%M:')
        self.minuto['font'] = 'Helvita 100'
        self.minuto.config(bg=bg, highlightthickness=0, borderwidth=0)

        self.segundo = Label()
        self.segundo.place(relx=self.posX+0.31, rely=self.posY+0.11)
        self.segundo['text'] = strftime('%S')
        self.segundo['font'] = 'Helvita 30'
        self.segundo.config(bg=bg, highlightthickness=0, borderwidth=0)

        self.troca()
