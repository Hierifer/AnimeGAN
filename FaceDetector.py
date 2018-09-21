#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:53:28 2018

@author: zijiachen
"""

import cv2
import sys
import os.path
from glob import glob

def detect(filename, opath, minSize= 48, output=96, cascade_file="lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)
        
    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    c = 0
    
    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(48, 48))
    for i, (x, y, w, h) in enumerate(faces):
        face = image[y: y + h, x:x + w, :]
        face = cv2.resize(face, (output, output))
        save_filename = '%s-%d.jpg' % (os.path.basename(filename).split('.')[0], i)
        
        cv2.imwrite(opath + "/" + save_filename, face)
        c += 1
    return c
    
def face_producer(ipath, opath, minSize= 48, output=96, cascade_file="lbpcascade_animeface.xml"):
    c = 0
    if os.path.exists(opath) is False:
        os.makedirs(opath)
    file_list = glob(ipath+'/*.jpg')
    for filename in file_list:
        c += detect(filename, opath, minSize, output)
    print("Extracted: " +str(c)+" faces from "+str(len(file_list))+" images")    
        
face_producer('imgs', 'face', output=180)