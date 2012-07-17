#!/usr/bin/python

from view.vioeConvertorGui import VioeConvertorGui, Tk

if __name__ == "__main__":

    root = Tk()
    root.title('VioeConvertor')
    app = VioeConvertorGui(root)
    root.mainloop()
