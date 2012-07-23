#!/usr/bin/python

from model.coordinateConvertor import CoordinateConvertor
from model.coordinateNormalizer import CoordinateNormalizer
from view.vioeConvertorGui import VioeConvertorGui
from view.badInputView import BadInputView
from view.convertedView import ConvertedView
from config.crs import crs
from config.messages import dms_input_error, decimal_input_error


class VioeController:
    '''Controller class'''

    def __init__(self, root):
        self.view = VioeConvertorGui(root)
        self.view.to_wgs84_button.config(command=self.convert_to_wgs84)
        self.view.to_lambert72_button.config(command=self.convert_to_lambert72)

    def convert_to_lambert72(self):
        try:
            normalizer = CoordinateNormalizer()
            x_src, y_src = normalizer.normalize_degree((self.view.x_coord.get(),
                                                        self.view.y_coord.get())
                                                        )
            convertor = CoordinateConvertor(crs['wgs84'][1],
                                            crs['lambert72'][1]
                                            )
            (x, y) = convertor.convert_point((x_src, y_src))
        except:
            BadInputView(dms_input_error)
        ConvertedView(crs['lambert72'][0], str(x), str(y))

    def convert_to_wgs84(self):
        try:
            normalizer = CoordinateNormalizer()
            x_src, y_src = normalizer.normalize_degree((self.view.x_coord.get(),
                                                        self.view.y_coord.get())
                                                        )
            convertor = CoordinateConvertor(crs['lambert72'][1],
                                            crs['wgs84'][1]
                                            )
            (x, y) = convertor.convert_point((x_src, y_src))
        except:
            BadInputView(decimal_input_error)
        ConvertedView(crs['wgs84'][0], str(x), str(y))
