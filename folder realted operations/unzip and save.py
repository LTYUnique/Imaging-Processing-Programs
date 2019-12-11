#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 15:39:46 2018

@author: lty
"""

import zipfile
import os
import natsort

data_path = '/home/lty/Downloads/3Dircadb1'
os.mkdir(os.path.join('/home/lty/Desktop','databsae'))
save_path = os.path.join('/home/lty/Desktop','databsae')
folder = natsort.natsorted(os.listdir(data_path))
for i in range(len(folder)):
    folder_path = os.path.join(data_path,folder[i])
    os.mkdir(os.path.join(save_path,folder[i]))
    files = natsort.natsorted(os.listdir(folder_path))
#    print(files)
    for j in range(len(files)):
#        print(files[j])
        if os.path.splitext(files[j])[1] == '.zip':
            files_path = os.path.join(folder_path,files[j])
            z = zipfile.ZipFile(files_path,'r')   
            z.extractall(os.path.join(save_path,folder[i]))
            print('Done!')
    
    