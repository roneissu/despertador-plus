from tkinter import Tk, Text
from views import time


if __name__ == '__main__':
    root = Tk()
    root.title('Despertador Plus')
    root.minsize(time.test(), 600)
    root.mainloop()
