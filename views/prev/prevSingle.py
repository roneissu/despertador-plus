from tkinter import *


class PrevisaoCard(Frame):

    font = ('Calibri', 12, 'bold')
    fontbig = ('Calibri', 18, 'bold')
    fonthuge = ('Calibri', 24, 'bold')

    def genFrame(self):

        self.card = Frame(self, bg=self.color)

        icon = Canvas(self.card, width=50, height=50, bd=4, relief='sunken')
        icon.grid(column=0, row=0, rowspan=4)

        clima = Label(self.card, text=self.forecast['clima'],
                      width=25, font=self.font, bg=self.color, anchor='center')
        clima.grid(column=0, row=4, sticky='nswe')

        temp = Label(self.card, text=str(
            self.forecast['temp'])+'°C', font=self.fonthuge, bg=self.color, anchor='center')
        temp.grid(column=1, row=0, rowspan=5, sticky='nswe')

        tempmax = Label(self.card, text=str(
            self.forecast['temp_max'])+'°C', font=self.fontbig, bg=self.color, anchor='center')
        tempmax.grid(column=2, row=0, rowspan=2, sticky='nswe')

        tempmin = Label(self.card, text=str(
            self.forecast['temp_min'])+'°C', font=self.fontbig, bg=self.color, anchor='center')
        tempmin.grid(column=2, row=3, rowspan=2, sticky='nswe')

        self.card.pack()

    def __init__(self, master=None, bg='light blue', forecast=None, **kargs):
        self.master = master
        self.color = bg
        super().__init__(master, bg=bg, **kargs)
        self.forecast = forecast
        self.genFrame()
