# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 16:10:57 2018

@author: admin
"""

import os
import natsort

path = '/media/lty/data/444/seg_liver_supervision_1_new_idea_no_change_loss'
path_new = '/media/lty/data/444/seg_liver_supervision_1_new_idea_no_change_loss_opening'
files = natsort.natsorted(os.listdir(path))
files_new = natsort.natsorted(os.listdir(path_new))
#print(files)
for i in range(len(files)):
    folder_name = files[i]
#    print(folder_name)
    if os.path.isdir(path_new):
        os.mkdir(os.path.join(path_new,folder_name))
        print('Done!')
