import numpy as np
from PIL import Image


class WriteOut():
    def __init__(self, imgName, writeColor):
        self.imgName = imgName
        self.writeColor = writeColor
        

    def createImg(self, width, height):
        pixels = np.zeros([height, width, 3], dtype=np.uint8)
        pixels.fill(255)

        img = Image.fromarray(pixels)
        img.save(self.imgName)


    def writePixels(self, pixelsToWrite, readIn):
        pixels = readIn.readPixels()
        for coord in pixelsToWrite:
            x, y = coord
            pixels[y][x].fill(self.writeColor)
        
        img = Image.fromarray(pixels)
        img.save(self.imgName)


    def writePatterns(self, readIn, pattern, rowAmount, columnAmount, xSpacing, ySpacing):
        pixels = readIn.readPixels()

        currentColumn = 0
        currentRow = 0

        minWidth = float("inf")
        minHeight = float("inf")
        maxWidth = float("-inf")
        maxHeight = float("-inf")

        for coord in pattern.formattedPixels:
            x, y, _ = coord

            minWidth = x if x < minWidth else minWidth
            minHeight = y if y < minHeight else minHeight
            maxWidth = x if x > maxWidth else maxWidth
            maxHeight = y if y > maxHeight else maxHeight
        

        for currentRow in range(rowAmount):
            for currentColumn in range(columnAmount):
                xOffset = (currentColumn) * (maxWidth - minWidth) + (currentColumn * xSpacing)
                yOffset = (currentRow) * (maxHeight - minHeight) + (currentRow * ySpacing)

                try:
                    for coord in pattern.formattedPixels:
                        x, y, color = coord
                        pixels[x + xOffset][y + yOffset] = color[:3]
                except IndexError:
                    break
        
        img = Image.fromarray(pixels)
        img.save(self.imgName)

