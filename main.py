from tkinter import *
from views.master import *


if __name__ == '__main__':
    root = Tk()
    mainView = Master(root, "Despertador Plus")

    root.minsize(800, 600)

    mainView.pack(fill='both', expand=1)

    root.mainloop()

