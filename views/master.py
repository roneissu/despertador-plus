from tkinter import *
import views.ambiente as am 

class Master(Frame):

    def __init__(self, master=None, title="", bg="pink", **kargs):
        self.master = master
        super().__init__(master, **kargs)
        self.master.title(title)
        self.amb = am.Ambiente(self, bd = 5, relief = "sunken")
        self.amb.grid(row=2, column=2, columnspan=2, sticky="NSWE", padx=5, pady=5)
       	self.columnconfigure(2, weight = 1)
        # self.amb.pack(fill = 'both', expand = 1)
