from tkinter import *

from views.ambiente import Ambiente
from views.relogio import Relogio


class Master(Frame):
    def __init__(self, master=None, title="", bg=""):
        self.master = master
        super().__init__(master)
        self.master.title(title)

        h = (master.winfo_screenheight()/2)
        w = (master.winfo_screenwidth()/2)

        relogio = Relogio(master, bg=bg)
        relogio.place(relheight=0.5, relwidth=0.5)
        relogio.config(bg=bg)
