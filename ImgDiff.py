# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:40:39 2020

@author: chris
"""
from PIL import Image
import glob
from pathlib import Path


sourceFiles = []
targetFiles= []

# Print png images in folder C:\Users\admin\
for filepath in glob.iglob(r'C:\Users\chris\Desktop\Images\Scource\*.jpg'):
    sourceFiles.append(filepath)
    
for filepath1 in glob.iglob(r'C:\Users\chris\Desktop\Images\Targer\*.jpg'):
    targetFiles.append(filepath1)
    
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