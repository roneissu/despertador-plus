from tkinter import *

from views.ambiente import Ambiente
from views.relogio import Relogio
from views.previsao import Previsao


class Master(Frame):
    def __init__(self, master=None, title="", bg="pink", **kargs):
        self.master = master
        super().__init__(master, **kargs)
        self.master.title(title)

        relogio = Relogio(master, bg=bg)
        relogio.place(relheight=0.5, relwidth=0.5)
        relogio.config(bg=bg)

        self.amb = Ambiente(self, bd=5, relief="sunken")
        self.amb.grid(row=2, column=2, columnspan=2,
                      sticky="NSWE", padx=5, pady=5)
        self.columnconfigure(2, weight=1)

        self.prev = Previsao(self, bd=5, relief="sunken")
        self.prev.grid(row=1, column=1, rowspan=2,
                       sticky='nswe', padx=5, pady=5)
        self.rowconfigure(1, weight=1)
        # self.amb.pack(fill = 'both', expand = 1)
