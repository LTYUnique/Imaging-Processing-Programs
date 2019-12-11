#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:49:29 2018

@author: lty
"""

from PIL import Image
import numpy as np
import os
import natsort
import scipy.io

path = '/home/lty/Desktop/label'
save_path = '/home/lty/Desktop/label_augmentation'

folders = natsort.natsorted(os.listdir(path))
for i in range(len(folders)):
    folders_path = os.path.join(path,folders[i])
    files = natsort.natsorted(os.listdir(folders_path))
    for j in range(len(files)):
        files_path = os.path.join(folders_path,files[j])
        imgs = Image.open(files_path)
        imgs_rotate = imgs.transpose(Image.FLIP_LEFT_RIGHT)
        scipy.misc.imsave(os.path.join(save_path,folders[i]+'_rotate')+'/'+files[j][0:-4]+'.png',imgs_rotate)
        print('Done!')











#im = Image.open(path)
##im_rotate = im.rotate(45)
#im_array = np.array(im)
#out = im_array.transpose(Image.FLIP_LEFT_RIGHT)
#out.show()