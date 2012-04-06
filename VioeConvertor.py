#!/usr/bin/python

from Tkinter import *
import tkMessageBox
import pyproj
from model.coordinateNormalizer import CoordinateNormalizer
from model.coordinateConvertor import CoordinateConvertor
import config.crs 

class VioeConvertorGui:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        frame_x = Frame(frame)
        frame_x.pack()

        frame_y = Frame(frame)
        frame_y.pack()

        frame_buttons = Frame(frame)
        frame_buttons.pack()

        self.x_label = Label(frame_x, text='Long/X:', width=10)
        self.x_label.pack(side=LEFT, padx=0, pady=10)
        self.x_coord = StringVar()
        self.x_coord_box = Entry(frame_x, textvariable=self.x_coord, width=30, bg='#fcfcfc', fg='#010101',bd=1)
        self.x_coord_box.pack(side=LEFT, padx=10, pady=10)

        self.y_label = Label(frame_y, text='Lat/Y:', width=10)
        self.y_label.pack(side=LEFT,padx=0, pady=10)
        self.y_coord = StringVar()
        self.y_coord_box = Entry(frame_y, textvariable=self.y_coord, width=30, bg='#fcfcfc', fg='#010101', bd=1)
        self.y_coord_box.pack(side=LEFT, padx=10, pady=10)

        self.to_lambert72_button = Button(frame_buttons, text='Naar Lambert72', command=self.convert_to_lambert72)
        self.to_lambert72_button.pack(side=LEFT, padx=10, pady=15)
        self.to_wgs84_button = Button(frame_buttons, text='Naar WGS84', command=self.convert_to_wgs84)
        self.to_wgs84_button.pack(side=LEFT, padx=10, pady=15)

    def convert_to_lambert72(self):
        try:
            normalizer = CoordinateNormalizer()
            x_src, y_src = normalizer.normalize_degree((self.x_coord.get(), self.y_coord.get()))
            convertor = CoordinateConvertor(crs.wgs84, crs.lambert72)
            (x, y) = convertor.convert_point((x_src, y_src))
        except:
            bad_input_error = "U kan enkel decimale graden ingeven of graden in het formaat:\nDD:MM:SS.SSSS..."
            tkMessageBox.showinfo('Invoerfout',bad_input_error)
        message = 'Lambertcoordinaten:\n' + str(x) + ', ' + str(y)
        tkMessageBox.showinfo('Lambert72', message)

    def convert_to_wgs84(self):
        try:
            normalizer = CoordinateNormalizer()
            x_src, y_src = normalizer.normalize_meter((self.x_coord.get(),self.y_coord.get()))
            convertor = CoordinateConvertor(crs.lambert72, crs.wgs84)
            (x, y) = convertor.convert_point((x_src, y_src))
        except:
            bad_input_error = 'U kan enkele numerieke waarden ingeven in meter.'
            tkMessageBox.showinfo('Invoerfout',bad_input_error)
        message = 'WGS84-coordinaten:\n' + str(x)+ 'Long' + ', ' + str(y) + 'Lat'
        tkMessageBox.showinfo('WGS84', message)



if __name__ == "__main__":

    root = Tk()
    root.title('VioeConvertor')
    app = VioeConvertorGui(root)
    root.mainloop()
