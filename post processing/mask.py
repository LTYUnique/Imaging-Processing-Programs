#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 16:06:32 2018

@author: lty
"""

import numpy as np
from PIL import Image
import os 
import scipy.io

path_mat = '/home/lty/LiTS/images_volumes'
path_png = '/home/lty/liverseg-2017-nipsws-master/LTY_cascaded_FCN_final_1_result/seg_liver_binary'
path_result_mat = '/home/lty/liverseg-2017-nipsws-master/LTY_cascaded_FCN_final_1_result/seg_liver_mat'
path_result_png = '/home/lty/liverseg-2017-nipsws-master/LTY_cascaded_FCN_stage_1_result/seg_liver'

files_mat = os.listdir(path_mat)
files_mat.sort(key=lambda x:int(x[:]))
#print(files_mat)
files_png = os.listdir(path_png)
files_png.sort(key=lambda x:int(x[:]))
#print(files_png)

for i in range(len(files_mat)):
    a_mat = os.path.join(path_mat,files_mat[i])
    b_mat = os.listdir(a_mat)
    b_mat.sort()
    a_png = os.path.join(path_png,files_png[i])
    b_png = os.listdir(a_png)
    b_png.sort()
    #print(b_mat,b_png)
    for j in range(len(b_mat)):
        c_mat = os.path.join(a_mat,b_mat[j])
        c_png = os.path.join(a_png,b_png[j])
        #print(c_mat,c_png)
        c_mat_array = scipy.io.loadmat(c_mat)['section']
        c_png_array = np.array(Image.open(c_png))
        new_array = c_mat_array*c_png_array
#        print(c_mat_array,c_png_array)
#        print(new_array)
#        print(new_array[:])
        scipy.io.savemat(os.path.join(path_result_mat,files_mat[i])+'/'+b_png[j][0:-4]+'.mat',{'section':new_array})
#        scipy.misc.imsave(os.path.join(path_result_png,files_mat[i])+'/'+b_png[j][0:-4]+'.png',new_array)
        print('done!')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        