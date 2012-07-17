#!/usr/bin/python


class CoordinateNormalizer:

    def __init__(self):
        pass

    def normalize_degree(self, point):
        x = self.dms_to_float(point[0]) if ':' in point[0] else float(point[0])
        y = self.dms_to_float(point[1]) if ':' in point[1] else float(point[1])
        return (x, y)

    def dms_to_float(self, dms_val):
        return sum(
            float(x) / 60 ** n for (n, x) in enumerate(dms_val.split(':')))

    def normalize_meter(self, point):
        x = float(point[0])
        y = float(point[1])
        return (x, y)

