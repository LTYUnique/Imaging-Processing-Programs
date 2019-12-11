#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 17:04:07 2018

@author: lty
"""

import numpy as np
from PIL import Image
import os 
import scipy.io
import natsort

path = '/home/lty/Desktop/111'
save_path = '/home/lty/Desktop/222'

files = natsort.natsorted(os.listdir(path))
for i in range(len(files)):
    files_path = os.path.join(path,files[i])
    imgs_array = np.array(Image.open(files_path))
    scipy.misc.imsave(save_path+'/'+np.str(i+1)+'.tif',imgs_array)
    print('Done!')