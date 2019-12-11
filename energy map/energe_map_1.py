#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:47:44 2018

@author: lty
"""

import os
import scipy.io
import natsort

path = '/media/lty/data/3_liverseg-2017-nipsws-master/LiTS_database_test/bb_images_volumes_alldatabase3_gt_nozoom_common_bb_test'
save_path = '/media/lty/data/3_liverseg-2017-nipsws-master/LiTS_database_test/energy_lesion_map_test'
#os.mkdir(save_path)
folders = natsort.natsorted(os.listdir(path))
for i in range(len(folders)):
    folders_path = os.path.join(path,folders[i])
    Nfolders_path = os.path.join(save_path,folders[i])
#    os.mkdir(Nfolders_path)
    files = natsort.natsorted(os.listdir(folders_path))
    b = 0
    for j in range(len(files)-3):
        b = b + 1
    for h in range(b,len(files)):
        files_path = os.path.join(folders_path,files[h])
        c = scipy.io.loadmat(files_path)['section']
        scipy.io.savemat(os.path.join(Nfolders_path,files[h]),{'section':c})  
    print('DONE!')