#!/usr/bin/python

from Tkinter import *
import pyproj
import tkMessageBox


class VioeConvertorGui:

    def __init__(self, master):
        self.wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
        self.lambert72 = pyproj.Proj('+proj=lcc +lat_1=51.16666723333333 +lat_2=49.8333339 +lat_0=90 +lon_0=4.367486666666666 +x_0=150000.013 +y_0=5400088.438 +ellps=intl +towgs84=106.869,-52.2978,103.724,-0.33657,0.456955,-1.84218,1 +units=m +no_defs ')

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
            convertor = CoordinateConvertor(self.wgs84, self.lambert72)
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
            convertor = CoordinateConvertor(self.lambert72, self.wgs84)
            (x, y) = convertor.convert_point((x_src, y_src))
        except:
            bad_input_error = 'U kan enkele numerieke waarden ingeven in meter.'
            tkMessageBox.showinfo('Invoerfout',bad_input_error)
        message = 'WGS84-coordinaten:\n' + str(x)+ 'Long' + ', ' + str(y) + 'Lat'
        tkMessageBox.showinfo('WGS84', message)



class CoordinateConvertor:

    def __init__(self, src_proj, trg_proj):
        self.src_proj = src_proj
        self.trg_proj = trg_proj

    def convert_point(self, src_point):
        x, y = pyproj.transform(self.src_proj, self.trg_proj, src_point[0], src_point[1])
        return (x, y)



class CoordinateNormalizer:

    def __init__(self):
        pass

    def normalize_degree(self, point):
        x = self.dms_to_float(point[0]) if ':' in point[0] else float(point[0])
        y = self.dms_to_float(point[1]) if ':' in point[1] else float(point[1])
        return (x, y)

    def dms_to_float(self, dms_val):
        return sum(float(x) / 60 ** n for (n, x) in enumerate(dms_val.split(':')))

    def normalize_meter(self, point):
        x =  float(point[0])
        y = float(point[1])
        return (x, y)



if __name__ == "__main__":

    root = Tk()
    root.title('VioeConvertor')
    app = VioeConvertorGui(root)
    root.mainloop()
