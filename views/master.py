from tkinter import *

from views.ambiente import Ambiente
from views.relogio import Relogio
from views.previsao import Previsao
from views.fotos import Fotos

class Master(Frame):
    def __init__(self, master=None, title="", bg="black", **kargs):
        self.master = master
        super().__init__(master, kargs)
        self.master.title(title)
        print('teste')
        self.relogio = Relogio(self, bg="black")
        self.relogio.grid(row=0, column=0, columnspan=3, rowspan=2, sticky="NSWE")
        print('teste2')
        self.foto = Fotos(self, bg="red")
        self.foto.grid(row=2, column=0, columnspan=3, rowspan=4, sticky="NSWE")
        print('teste3')
        self.prev = Previsao(self, bg="black")
        self.prev.grid(row=0, column=3, columnspan=2, rowspan=5, sticky="NSWE")
        # self.prev.place(relx=0.5, rely=0)
        # self.prev.config(bg=bg)

        self.amb = Ambiente(self, bg="black")
        self.amb.grid(row=5, column=3, columnspan=2, sticky="NSWE")
        # self.amb.place(relx=0, rely=0.5)
        # self.amb.config(bg=bg)
        # self.amb.pack(fill = 'both', expand = 1)

        for i in [0,1,2,3,4]:
            self.columnconfigure(i, weight=1)
        for i in [0,1,2,3,4,5]:
            self.rowconfigure(i, weight=1)
