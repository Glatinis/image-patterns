import os
import subprocess
from readin import ReadIn
from writeout import WriteOut
from pattern import Pattern


IMGNAME = "image.png"

readIn = ReadIn(IMGNAME)
writeOut = WriteOut(IMGNAME, 0)

writeOut.createImg(1280, 1080)

squarePattern = Pattern("patterns/square.png")
garntPattern = Pattern("patterns/garnt.png")

writeOut.writePatterns(readIn, squarePattern, 100, 100, 0, 0)


paintPath = os.path.splitdrive(os.path.expanduser("~"))[0]+r"\WINDOWS\system32\mspaint.exe"
subprocess.Popen(f"{paintPath} {IMGNAME}")