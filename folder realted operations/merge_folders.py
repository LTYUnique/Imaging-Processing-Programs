# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 15:32:36 2018

@author: admin
"""
import scipy.io
import natsort
import os
import numpy as np
from PIL import Image

path = '/home/lty/liverseg-2017-nipsws-master/LiTS_database/liver_seg' 
#path = '/home/lty/liverseg-2017-nipsws-master/LiTS_database/LBP_images_volumes_tif_test'
save_path = '/home/lty/liverseg-2017-nipsws-master/LiTS_database/train'
#save_path = 'D:\LBP_666'            

folder = natsort.natsorted(os.listdir(path))  
for i in range(len(folder)):
    files_path = os.path.join(path,folder[i])
    files = natsort.natsorted(os.listdir(files_path))
    for j in range(len(files)):
        a = os.path.join(files_path,files[j])  
        img = Image.open(a)
        img_array = np.array(img)
#        print(img_array)
#        scipy.misc.imsave(save_path+'/'+folder[i]+'_'+files[j][0:-4]+'.tif',img_array) #保存图像
        scipy.misc.imsave(save_path+'/'+folder[i]+'_'+files[j][0:-4]+'_mask'+'.tif',img_array)#保存标签
        print('Done!')