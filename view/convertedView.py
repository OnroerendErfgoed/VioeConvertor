#!/usr/bin/python

import tkMessageBox


class ConvertedView:
    '''GUI screen showing converted coordinates'''

    def __init__(self, crs, x, y):
        self.message = 'Coordinaten in ' + crs + ':\n' + x + ', ' + y
        tkMessageBox.showinfo('crs', self.message)
