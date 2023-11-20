import glob
import datetime
from PIL import Image
import subprocess
import sys
import shutil
import os
import hashlib


"""A script Jon uses to sort photos/movies from multiple devices
according to date taken (but checking first if we would overwrite
an existing file that might have been edited)
"""

if "apply" in sys.argv:
    DRY_RUN = False
else:
    DRY_RUN = True
    print("This is a dry run. Use \n\tpython image_sort.py apply\nto apply")
photoLib = "."
logFileName = 'last.log'
log = open(logFileName, 'w')

paths = [
    "unsorted/",
    #"/Users/lpzjwp/Documents/SM-G950F_01eb6c473a235/storage_3482-7826_DCIM/Camera",
    ]
files = []
for thisFolder in paths:
	files.extend(glob.glob(os.path.join(thisFolder, "*")))
#files = ["unsorted/IMG_1363.JPG"]

TAGS = {0x9003:"DateTimeOriginal",
        0x9004:"DateTimeDigitized",
        0x0132:"DateTime",
        }

def timeStr(timestamp):
    return datetime.datetime.fromtimestamp(
            timestamp).strftime("%Y:%m:%d:%H:%M:%S")

def getImageCreated(filename):
    dateCreate= timeStr(os.stat(filename).st_ctime)  # created time
    dateMod = timeStr(os.stat(filename).st_mtime) # strangely sometimes earlier!!? :-/
    dateString = min(dateCreate, dateMod)
    #print("starting: {}".format(dateString))
    try:
        exifDict = Image.open(filename)._getexif()
    except IOError:
        return -1
    if exifDict is None:
        return None
    for (tagIndex, value) in exifDict.iteritems():
        if tagIndex in TAGS:
            #print("found tag {}: {}".format(TAGS[tagIndex], value))
            if type(value)==tuple:
                value = value[0]
            value = value.replace(" ", ":")
            if value<dateString:
                dateString = value
    return dateString

def getMovDateMeta(filename):
    proc = subprocess.Popen(["ffmpeg","-i", filename, "-f", "ffmetadata"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    out, err = proc.communicate()
    dateStr = timeStr = ""
    for line in err.split("\n"):
        if "creation_time" in line:
            ## looks like "    creation_time   : 2015-10-03 11:37:24"
            for thisWord in line.split():
                if "-" in thisWord:  # ffmpeg gives date as 2015-20-12
                    dateStr = thisWord.replace("-", ":")
                elif ":" in thisWord:  # ffmpeg gives date
                   timeStr = thisWord
    if dateStr:  # if no date then return None
        return dateStr+":"+timeStr

def get_md5(filename):
    return hashlib.md5(open(filename).read()).hexdigest()

for inFile in files:
    print ".",
    sys.stdout.flush()
    log.write(inFile)
    inFolder, filename = os.path.split(inFile)
    # get earliest recorded date
    dateString = None
    if inFile.lower().endswith(".jpg"):
        dateString = getImageCreated(inFile)
    elif inFile.lower()[-4:] in [".mov", ".mp4"]:
        dateString = getMovDateMeta(inFile)
    else:
        log.write("\tNOT AN IMAGE/MOVIE\n")
        continue
    if dateString is None:
        log.write("\tNO DATE INFO\n")
        continue
    elif dateString==-1:
        log.write("\tERROR WITH FILE\n")
        continue
    year, month = dateString.split(":")[0:2]
    outDir = os.path.abspath(os.path.join(photoLib, year, month))
    outFile = os.path.join(outDir, filename)
    if os.path.isfile(outFile):
        hashIn = get_md5(inFile)
        hashOut = get_md5(outFile)
        if hashIn==hashOut:
            if timeStr(os.stat(inFile).st_mtime) != timeStr(os.stat(outFile).st_mtime):
                # same file but incorrect file datestamp
                if not DRY_RUN:
                    shutil.copy2(inFile, outFile)  # copy keeping filestats
                log.write("\tupdating\t{}\n".format(outFile))
            else:
                log.write("\texists\t{}\n".format(outFile))
        else:
            log.write("\tDIFFERS\t{}\n".format(outFile))
            log.write("{}\n".format(hashIn))
            log.write("{}\n".format(hashOut))
    else:
        if not DRY_RUN:
            if not os.path.isdir(outDir):
                os.makedirs(outDir)
            shutil.copy2(inFile, outFile)  # copy keeping m
        log.write("\t->\t{}\n".format(outFile))
print("\nFinished sort. Info in {}".format(logFileName))
