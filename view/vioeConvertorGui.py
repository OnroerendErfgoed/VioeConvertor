#!/usr/bin/python

from Tkinter import *


class VioeConvertorGui:
    '''GUI coordinate input screen'''

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
        self.x_coord_box = Entry(frame_x,
                                 textvariable=self.
                                 x_coord, width=30,
                                 bg='#fcfcfc',
                                 fg='#010101',
                                 bd=1)
        self.x_coord_box.pack(side=LEFT, padx=10, pady=10)

        self.y_label = Label(frame_y, text='Lat/Y:', width=10)
        self.y_label.pack(side=LEFT, padx=0, pady=10)
        self.y_coord = StringVar()
        self.y_coord_box = Entry(frame_y,
                                 textvariable=self.
                                 y_coord,
                                 width=30,
                                 bg='#fcfcfc',
                                 fg='#010101',
                                 bd=1)
        self.y_coord_box.pack(side=LEFT, padx=10, pady=10)

        self.to_lambert72_button = Button(frame_buttons,
                                          text='Naar Lambert72',
                                          )
        self.to_lambert72_button.pack(side=LEFT, padx=10, pady=15)

        self.to_wgs84_button = Button(frame_buttons,
                                      text='Naar WGS84',
                                      )
        self.to_wgs84_button.pack(side=LEFT, padx=10, pady=15)
