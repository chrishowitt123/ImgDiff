from PIL import Image
import glob
from pathlib import Path
import os, sys

sourceFolder = r'C:\Users\chris\Desktop\Images\Scource\*.jpg'
targetFolder = r'C:\Users\chris\Desktop\Images\Target\*.jpg'

sourceFiles = []
targetFiles= []

# Print png images in folder C:\Users\admin\
for filepath in glob.iglob(sourceFolder):
    sourceFiles.append(filepath)
    
for filepath1 in glob.iglob(targetFolder):
    targetFiles.append(filepath1)

from PIL import Image
import os, sys
import glob

root_dir = "/.../.../.../"


for filename in glob.iglob(sourceFolder, recursive=True):
    print(filename)
    im = Image.open(filename)
    imResize = im.resize((1748 ,2480), Image.ANTIALIAS)
    imResize.save(filename , 'JPEG', quality=90)

for filename in glob.iglob(targetFolder, recursive=True):
    print(filename)
    im = Image.open(filename)
    imResize = im.resize((1748 ,2480), Image.ANTIALIAS)
    imResize.save(filename , 'JPEG', quality=90)
    
p = 1
    
for s, t in zip(sourceFiles, targetFiles):
    s = Image.open(s)
    t = Image.open(t)
    assert s.mode == t.mode, "Different kinds of images."
    assert s.size == t.size, "Different sizes."
 
    pairs = zip(s.getdata(), t.getdata())
    if len(s.getbands()) == 1:
    # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
 
    ncomponents = s.size[0] * s.size[1] * 3

    
    print (f" Page {p} Difference (percentage):", (dif / 255.0 * 100) / ncomponents)
    
    p += 1
