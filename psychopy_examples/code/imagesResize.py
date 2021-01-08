from __future__ import division
import glob
import os
from PIL import Image

#This script changes all images found to have a maximum
#height/width of 500 pixels (whichever dimension is larger)

filenames = glob.glob("images/*.jpg")

for thisFilename in filenames:
    folder, filename = os.path.split(thisFilename)
    print folder, filename
    newFilename, extension = os.path.splitext(filename)
    newFilename += ".png"
    thisIm = Image.open(thisFilename)
    
    # the tricky thing here is to keep aspect ratio
    # to be constant (resize both dimensions equally)
    w, h = thisIm.size
    if w>h:
        scale = 500/w
    else:
        scale = 500/h
    newSize = (int(scale*w), int(scale*h))
    newIm = thisIm.resize(newSize)
    
    newIm.save(os.path.join('newImages',newFilename))
    
    
    