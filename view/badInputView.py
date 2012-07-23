#/usr/bin/python

import tkMessageBox


class BadInputView:
    '''GUI bad input message'''

    def __init__(self, message):
        self.message = message
        tkMessageBox.showinfo('Invoerfout', message)
