from tkinter import *


class Master(Frame):

    def __init__(self, master=None, title="", bg="pink"):
        self.master = master
        super().__init__(master)
        self.master.title(title)
