#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 21:38:51 2018

@author: lty
"""

import os
import scipy.io
import natsort
#import numpy as np

path = '/media/lty/data/3_liverseg-2017-nipsws-master/LiTS_database_test/bb_images_volumes_alldatabase3_gt_nozoom_common_bb_test'
save_path = '/media/lty/data/3_liverseg-2017-nipsws-master/LiTS_database_test/energy_lesion_map_test'

folders = natsort.natsorted(os.listdir(path))
for i in range(len(folders)):
    folders_path = os.path.join(path,folders[i])
    save_folders_path = os.path.join(save_path,folders[i])
    files = natsort.natsorted(os.listdir(folders_path))
    for j in range(0,2):
        files_path = os.path.join(folders_path,files[j])
        c = scipy.io.loadmat(files_path)['section']
        scipy.io.savemat(os.path.join(save_folders_path,files[j]),{'section':c}) 
        print('Done!')
        

        