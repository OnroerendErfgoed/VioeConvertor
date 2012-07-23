#!/usr/bin/python
import pyproj


class CoordinateConvertor:
    """Wrapper class around pyproj.transform"""

    def __init__(self, src_proj, trg_proj):
        """Initialize CoordinateConvertor object

        Arguments:
        src_proj: source coordinate system in proj4 notation
        trg_proj: target projection in proj4 notation

        """

        self.src_proj = pyproj.Proj(src_proj)
        self.trg_proj = pyproj.Proj(trg_proj)

    def convert_point(self, src_point):
        """Converts a point using objects source and target crs

        Arguments:
        src_point: a pair (list or tupple) representing (x,y) coordinates

        """
        x, y = pyproj.transform(self.src_proj,
                                self.trg_proj,
                                src_point[0],
                                src_point[1])
        return (x, y)
