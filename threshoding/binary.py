#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:23:23 2018

@author: lty
"""

import os
import numpy as np
import natsort 
import scipy.misc
from PIL import Image

result_path = '/media/lty/data/3_liverseg-2017-nipsws-master/results/seg_liver_test'
binary_path = '/media/lty/data/3_liverseg-2017-nipsws-master/results/seg_liver_test_binary'

folders = natsort.natsorted(os.listdir(result_path))
for i in range(len(folders)):
    folders_dirs = os.path.join(result_path,folders[i])
    files = natsort.natsorted(os.listdir(folders_dirs))
    for j in range(len(files)):
        files_dirs = os.path.join(folders_dirs,files[j])
        img = Image.open(files_dirs) 
#        img_1 = img.resize((256,256))
        img_array = np.array(img)
        img_array[img_array < 230] = 0
        img_array[img_array >= 230] = 255
        img_array[-1][-1] = 0
        img_array[-1][0] = 0
        img_array[0][0] = 0
        img_array[0][-1] = 0
#        print(img_array)
        scipy.misc.imsave(os.path.join(binary_path,folders[i])+'/'+files[j][0:-4]+'.png',img_array)
#        scipy.io.savemat(os.path.join(binary_path,folders[i])+'/'+files[j][0:-4]+'.mat',{'section':img_array})
        print('Done!')  
    