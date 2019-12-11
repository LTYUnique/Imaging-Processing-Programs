#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 20:50:24 2018

@author: lty
"""

import os
import scipy.io
import natsort
import numpy as np

path = '/media/lty/data/3_liverseg-2017-nipsws-master/LiTS_database_test/bb_images_volumes_alldatabase3_gt_nozoom_common_bb_test'
save_path = '/media/lty/data/3_liverseg-2017-nipsws-master/LiTS_database_test/energy_lesion_map_test'
#os.mkdir(save_path)
#c = []
folders = natsort.natsorted(os.listdir(path))
for i in range(len(folders)):
    folders_path = os.path.join(path,folders[i])
    save_folders_path = os.path.join(save_path,folders[i])
#    os.mkdir(save_folders_path)
    files = natsort.natsorted(os.listdir(folders_path))
#    print(files)
    a = 0
    b = 0
    for j in range(len(files)-5):
        for z in range(j+1, j+6):
#            c.append(z)
#            print(c)
            files_path = os.path.join(folders_path,files[z]) #每张图片的路径
            a = a + scipy.io.loadmat(files_path)['section']
        a = a/5
        scipy.io.savemat(os.path.join(save_folders_path,files[j+2]),{'section':a})
        print('done!')
        
