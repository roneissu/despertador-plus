from datetime import datetime
from time import strftime
from tkinter import *


class SegundoBarra(Frame):
    def troca(self, segundo=0):
        self.segundoBar.place(rely=0.9-segundo/80, relheight=segundo/80)


    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.segundoBar = Label(self, bg="white")
        self.segundoBar.place(relx=0.2, rely=0.1, relwidth=0.3)


class Relogio(Frame):
    def troca(self):
        self.hora['text'] = strftime('%H:')
        self.minuto['text'] = strftime('%M')
        self.segundo.troca(datetime.now().second)

        self.after(500, self.troca)

    def __init__(self, master=None, bg="black", **kwargs):
        self.master = master
        super().__init__(master, kwargs, bg=bg)
        self.bg = bg

        self.hora = Label(self, bg=bg, fg="white")
        self.hora.grid(row=1, column=1, sticky="NSWE")
        self.hora['font'] = 'Helvita 140 bold'

        self.minuto = Label(self, bg=bg, fg="white")
        self.minuto.grid(row=1, column=2, sticky="NSWE")
        self.minuto['font'] = 'Helvita 140'

        self.segundo = SegundoBarra(self, bg=bg)
        self.segundo.grid(row=0, column=3, rowspan=3, sticky="NSWE")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(3, weight=1)

        self.troca()
