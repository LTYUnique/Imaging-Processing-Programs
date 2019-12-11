# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 20:31:07 2018

@author: admin
"""

import os
import scipy.io
import natsort
import numpy as np

save_path = '/home/lty/liverseg-2017-nipsws-master/LiTS_database/energy_map(0,255)'
#os.mkdir(save_path)
path = '/home/lty/liverseg-2017-nipsws-master/LiTS_database/images_volumes'
folders = natsort.natsorted(os.listdir(path))
a = 0
for i in range(len(folders)):
    folders_path = os.path.join(path,folders[i])
    Nfolders_path = os.path.join(save_path,folders[i])
#    os.mkdir(Nfolders_path)
    files = natsort.natsorted(os.listdir(folders_path))
    a = 0
    b = 0
    for j in range(len(files)-4):
        b = b + 1
        for z in range(j, j+5):
            files_path = os.path.join(folders_path,files[z]) #每张图片的路径
            a = a + scipy.io.loadmat(files_path)['section']
        a = a/5
        scipy.io.savemat(os.path.join(Nfolders_path,files[j]),{'section':a}) #保存图像
#        for h in range(b,len(files)):
#            c = scipy.io.loadmat(files_path)['section']
#            scipy.io.savemat(os.path.join(Nfolders_path,files[h]),{'section':c})  
        print('DONE!')
        
# a = 0
#c = 0
#d = 0
#for j in range(len(files)-4):
#    a = a + 1
#    for z in range(j, j+5):
#        b.append(files[z])
#        b_dirs = os.path.join(path,files[z])
#        d = d + scipy.io.loadmat(b_dirs)['section']
#    d = d/5
#    scipy.io.savemat(save_path+'\\'+files[z],{'section':d})
#    print('Done!')
#for h in range(a,len(files)):
#    c = c + 1
#    b.append(files[h])       
#            
