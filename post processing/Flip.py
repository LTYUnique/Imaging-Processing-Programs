#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 19:52:17 2018

@author: lty
"""

import os
from PIL import Image
import natsort
import numpy as np
import scipy.misc
import SimpleITK as sitk

path = '/media/lty/data/333/3'
save_path = '/media/lty/data/333/3_new'

a = natsort.natsorted(os.listdir(path))

for i in range(len(a)):
    folders_dir = os.path.join(path,a[i])
    files = natsort.natsorted(os.listdir(folders_dir))
    for j in range(len(files)):
        files_dir = os.path.join(folders_dir,files[j])
        im = Image.open(files_dir)
        im = im.transpose(Image.FLIP_TOP_BOTTOM)
#        im = im.transpose(Image.FLIP_LEFT_RIGHT)
        im = im.transpose(Image.ROTATE_270)

        
        files_array = np.array(im)
        scipy.misc.imsave(os.path.join(save_path,a[i])+'/'+files[j][0:-4]+'.png',im)
        print('done!')
