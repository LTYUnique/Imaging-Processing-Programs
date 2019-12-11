#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 19:25:22 2018

@author: lty
"""

import os
import natsort
import numpy as np
import scipy.io
from PIL import Image

path = '/home/lty/Desktop/save_2'
save_path = '/home/lty/Desktop/save_3'
folders = natsort.natsorted(os.listdir(path))
for i in range(len(folders)):
    folders_path = os.path.join(path,folders[i])
    files = natsort.natsorted(os.listdir(folders_path))
    for j in range(len(files)):
        files_path = os.path.join(folders_path,files[j])
        img = Image.open(files_path)
        img_array = np.array(img)
        scipy.io.savemat(os.path.join(save_path,folders[i])+'/'+files[j][0:-4]+'.mat',{'section':img_array})
        print('Done!')
    

