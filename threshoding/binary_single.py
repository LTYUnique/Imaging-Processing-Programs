#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:44:22 2018

@author: lty
"""

import os
import numpy as np
import natsort 
import SimpleITK as sitk
import scipy.misc
from PIL import Image

label_path = '/home/lty/liverseg-2017-nipsws-master/FCN_4_final_result/seg_liver/108_1'
result_path = '/home/lty/Desktop/binary_new/108_1'

label_files = natsort.natsorted(os.listdir(label_path))
for i in range(len(label_files)):
    label_files_path = os.path.join(label_path,label_files[i])
    img = Image.open(label_files_path)  
    img_array = np.array(img)
#    print(img_array)
    img_array[img_array < 225] = 0
    img_array[img_array >= 225] = 255
#    print(img_array)
    scipy.misc.imsave(result_path+'/'+label_files[i],img_array)
    print('Done!')

