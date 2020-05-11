#!/usr/bin/env python3

import os, sys
from cv2 import *

def writeFile(name, target, resolution=(256, 256)):
    img = imread(name)
    imwrite(target, resize(img, resolution))

filename = sys.argv[1]
filenamePNG = ".".join(filename.split(".")[:len(filename.split("."))-1]) + ".png"

x = y = 256
if len(sys.argv) >= 4:
    x = int(sys.argv[2])
    y = int(sys.argv[3])

if os.path.isfile(filename):
    writeFile(filename, filenamePNG, (x,y))
elif os.path.isdir(filename):
    files = os.listdir(filename)
    for file in files:
        writeFile(filename + "/" + file, filename + "/" + ".".join(file.split(".")[:len(file.split("."))-1]) + ".png", (x,y))
else:
    raise RuntimeError("{} is not a valid file.".format(filename))

if not os.path.isdir(filename) and filename.endswith(".png"):
    os.remove(filename)
