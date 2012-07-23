#!/usr/bin/python

from Tkinter import Tk
from controller.vioeController import VioeController

if __name__ == "__main__":

    root = Tk()
    root.title('VioeConvertor')
    app = VioeController(root)
    root.mainloop()
