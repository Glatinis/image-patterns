import numpy as np
from PIL import Image


class ReadIn():
    def __init__(self, imgName):
        self.imgName = imgName
    
    def readPixels(self):
        img = Image.open(self.imgName)
        pixels = np.asarray(img)

        return pixels
