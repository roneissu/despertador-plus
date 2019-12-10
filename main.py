from tkinter import Tk
from views.master import Master


if __name__ == '__main__':
    root = Tk()
    root.attributes('-fullscreen', True)
    # root.minsize(1280, 720)

    main_view = Master(root, "Despertador Plus", bg="black")
    main_view.pack(fill="both", expand=1)

    root.mainloop()
