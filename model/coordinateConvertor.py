#!/usr/bin/python
import pyproj

class CoordinateConvertor:

    def __init__(self, src_proj, trg_proj):
        self.src_proj = src_proj
        self.trg_proj = trg_proj

    def convert_point(self, src_point):
        x, y = pyproj.transform(self.src_proj, self.trg_proj, src_point[0], src_point[1])
        return (x, y)