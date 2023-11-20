from __future__ import division
import glob
import os
import time
from PIL import Image, ImageFilter

filenames = glob.glob("images/*.jpg")
blurLevel = 4

gaussBlur = ImageFilter.GaussianBlur(radius=blurLevel)

for thisFilename in filenames:
    
    # disect the filename to create a new one
    newFilename, extension = os.path.splitext(thisFilename)
    newFilename += "blur%i.png" %(blurLevel)
    
    # open our image
    t0 = time.time()
    thisIm = Image.open(thisFilename)
    t1 = time.time()
    # blur it
    filtered = thisIm.filter(gaussBlur)
    t2 = time.time()
    # save
    filtered.save(newFilename)
    
    print('took %.3f seconds to load and %.3f secs to filter' %(t1-t0, t2-t1))
    
    