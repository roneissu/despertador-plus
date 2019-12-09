from tkinter import *
from views.master import *


if __name__ == '__main__':
    root = Tk()
    mainView = Master(root, "Despertador Plus", bd = 2, relief = 'raised')

<<<<<<< Updated upstream
    root.minsize(800, 600)

    mainView.pack(fill='both', expand=1)
=======
    main_view = Master(root, "Despertador Plus",
                       bg="#fbfbfb", bd=5, relief='raised')
    main_view.pack(fill = "both", expand = 1)
>>>>>>> Stashed changes

    root.mainloop()

