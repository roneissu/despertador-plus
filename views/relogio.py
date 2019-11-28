from datetime import datetime
from time import strftime
from tkinter import *


class Relogio(Frame):
    def troca(self):
        self.hora['text'] = strftime('%H:')
        self.minuto['text'] = strftime('%M')
        # self.segundo['text'] = strftime('%S')
        self.segundoBar.place(
            rely=(0.35-datetime.now().second/240), relheight=(datetime.now().second/240))

        self.after(500, self.troca)

    def __init__(self, master=None, bg=""):
        self.master = master
        super().__init__(master)

        self.posX = 0.01
        self.posY = 0.105

        self.hora = Label()
        self.hora.place(relx=self.posX, rely=self.posY)
        self.hora['font'] = 'Helvita 140 bold'
        self.hora.config(bg=bg, highlightthickness=0, borderwidth=0)

        self.minuto = Label()
        self.minuto.place(relx=self.posX+0.25, rely=self.posY)
        self.minuto['font'] = 'Helvita 140'
        self.minuto.config(bg=bg, highlightthickness=0, borderwidth=0)

        # self.segundo = Label()
        # self.segundo.place(relx=self.posX+0.43, rely=self.posY+0.16)
        # self.segundo['font'] = 'Helvita 40'
        # self.segundo.config(bg=bg, highlightthickness=0, borderwidth=0)

        self.segundoBar = Label()
        self.segundoBar.place(relx=self.posX+0.45, relwidth=0.02)
        self.segundoBar.config(bg="#606060")

        self.troca()
