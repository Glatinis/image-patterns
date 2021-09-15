from PIL import Image
import numpy as np

class Pattern():
    def __init__(self, path):
        self.path = path
        self.pixels = np.asarray(Image.open(self.path))
        self.formattedPixels = []
        for rowIndex, row in enumerate(self.pixels):
            for columnIndex, column in enumerate(row):
                coord = (rowIndex, columnIndex, list(column))
                self.formattedPixels.append(coord)