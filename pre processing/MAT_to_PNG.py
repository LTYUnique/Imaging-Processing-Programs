#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 19:27:33 2018

@author: lty
"""

import numpy as np
from PIL import Image
import os 
import scipy.io
import natsort

path = '/home/lty/Desktop/crf/1'
save_path = '/home/lty/Desktop/crf/img_png_105'

folders = natsort.natsorted(os.listdir(path))
for i in range(len(folders)):
    folders_path = os.path.join(path,folders[i])
    files = natsort.natsorted(os.listdir(folders_path))
    for j in range(len(files)):
        files_path = os.path.join(folders_path,files[j])
        files_array = scipy.io.loadmat(files_path)['section']
        scipy.misc.imsave(os.path.join(save_path,folders[i])+'/'+files[j][0:-4]+'.png',files_array)
        print('Done!')





#files = natsort.natsorted(os.listdir(path))
#for i in range(len(files)):
#    files_path = os.path.join(path,files[i])
#    files_array = scipy.io.loadmat(files_path)['section']
#    scipy.misc.imsave(save_path+'/'+files[i][0:-4]+'.png',files_array)
#    print('Done!')
