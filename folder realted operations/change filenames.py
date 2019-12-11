#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#coding=utf-8 
"""
Created on Thu May 24 09:50:49 2018

@author: lty
"""

import os 
#import string
#from shutil import move

path = '/home/lty/Desktop/interval_0'  
files = os.listdir(path)                           #get subfolders' names
for i in files:
    f1 = os.path.join(path,os.path.basename(i))
    F = os.listdir(f1)                             #get all files' names under the subfolder
    #F.sort(key=lambda x:int(x[:-4]))              #rank all files'names from smallest to largest
    os.chdir('/home/lty/Desktop/interval_0/%s'%i)  #change the work path to current path
    for oldname in F:
        print(oldname)
        portion = os.path.splitext(oldname)        #split filename and filename extension
        if portion[1] ==".png":
             newname = portion[0]+".mat"
             #print(newname)
             os.rename(oldname,newname)
             
             print('Done!')
             
             
             
