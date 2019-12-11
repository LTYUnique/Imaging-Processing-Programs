# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:42:28 2018

@author: admin
"""

import os
from PIL import Image
import natsort
import numpy as np
import scipy.io

path = '/home/lty/Desktop/his_new_result_binary'
save_path = '/home/lty/Desktop/his_resize_result'

folders = natsort.natsorted(os.listdir(path))
for i in range(len(folders)):
    folders_path = os.path.join(path,folders[i])
    files = natsort.natsorted(os.listdir(folders_path))
#    print(folders_path)
    for j in range(len(files)):
        files_path = os.path.join(folders_path,files[j])
#        print(files_path)
        img = Image.open(files_path)
        new_img = img.resize((256,256))
        new_img_array = np.array(new_img)
        scipy.misc.imsave(save_path+'/'+folders[i]+'/'+files[j][0:-4]+'.png',new_img_array)
#        scipy.misc.imsave(os.path.join(save_path,folders[i])+files[j],new_img_array)
#        new_img.save(os.path.join(folders_path,files[j]))
        print('Done!')
        
    