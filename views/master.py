from tkinter import *

from views.ambiente import Ambiente
from views.relogio import Relogio
from views.previsao import Previsao


class Master(Frame):
    def __init__(self, master=None, title="", bg="pink", **kargs):
        self.master = master
        super().__init__(master, kargs)
        self.master.title(title)

        self.relogio = Relogio(self, bg="blue")
        self.relogio.grid(row=0, column=0, columnspan=3, rowspan=2, sticky="NSWE")

        self.foto = Frame(self, bg="black")
        self.foto.grid(row=2, column=0, columnspan=3, rowspan=4, sticky="NSWE")

        # self.prev = Previsao(self, bg="blue")
        self.prev = Frame(self, bg="red")
        self.prev.grid(row=0, column=3, columnspan=2, rowspan=5, sticky="NSWE")
        # self.prev.place(relx=0.5, rely=0)
        # self.prev.config(bg=bg)

        # self.amb = Ambiente(self, bg="red")
        self.amb = Frame(self, bg="green")
        self.amb.grid(row=5, column=3, columnspan=2, sticky="NSWE")
        # self.amb.place(relx=0, rely=0.5)
        # self.amb.config(bg=bg)
        # self.amb.pack(fill = 'both', expand = 1)

        for i in range(5):
            self.columnconfigure(i, weight=1)
        for i in range(6):
            self.rowconfigure(i, weight=1)
        # self.columnconfigure(0, weight=1)
        # self.columnconfigure(2, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)
