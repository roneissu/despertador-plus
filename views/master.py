from tkinter import *

from views.ambiente import Ambiente
from views.relogio import Relogio
from views.previsao import Previsao


class Master(Frame):
    def __init__(self, master=None, title="", bg="pink", **kargs):
        self.master = master
        super().__init__(master, **kargs)
        self.master.title(title)

        self.relogio = Relogio(master, bg=bg)
        self.relogio.place(relheight=0.5, relwidth=0.5)
        self.relogio.config(bg=bg)

        self.amb = Ambiente(master, bd=5, relief="sunken")
        # self.amb.grid(row=2, column=2, columnspan=2,
        #               sticky="NSWE", padx=5, pady=5)
        # self.columnconfigure(2, weight=1)
        self.amb.place(relx=0, rely=0.5)
        self.amb.config(bg=bg)

        self.prev = Previsao(master, bd=5, relief="sunken")
        # self.prev.grid(row=1, column=1, rowspan=2,
        #                sticky='nswe', padx=5, pady=5)
        # self.rowconfigure(1, weight=1)
        self.prev.place(relx=0.5, rely=0)
        self.prev.config(bg=bg)
        # self.amb.pack(fill = 'both', expand = 1)
