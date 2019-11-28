from tkinter import Tk
from views.master import Master


if __name__ == '__main__':
    root = Tk()
    root.attributes('-fullscreen', True)

    main_view = Master(root, "Despertador Plus", bg="#fbfbfb", bd = 2, relief = 'raised')
    main_view.pack()

    root.mainloop()

