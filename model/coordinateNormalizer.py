#!/usr/bin/python


class CoordinateNormalizer:
    """Class to normalize coordinates to pairs of floats"""

    def __init__(self):
        pass

    def normalize_degree(self, point):
        """Converts coordinate pair from degree minutes seconds to decimal.

        Arguments:
        point: two element tupple or list of the x (longitude) and y (latitude)
        coordinates

        """
        x = self.dms_to_float(point[0]) if ':' in point[0] else float(point[0])
        y = self.dms_to_float(point[1]) if ':' in point[1] else float(point[1])
        return (x, y)

    def dms_to_float(self, dms_val):
        """Accepts a single value in D:M:S and returns in a decimal format."""
        return sum(
            float(x) / 60 ** n for (n, x) in enumerate(dms_val.split(':')))

    def normalize_meter(self, point):
        """Acccepts a pair of values which are returned as a pairof floats"""
        x = float(point[0])
        y = float(point[1])
        return (x, y)
