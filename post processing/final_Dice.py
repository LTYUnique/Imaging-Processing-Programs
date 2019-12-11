#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:42:38 2018

@author: lty
"""

import SimpleITK as sitk
import os
import natsort
import numpy as np

label_path = '/home/lty/Desktop/label'
binary_path = '/media/lty/办公/liverseg-2017-nipsws-master/results/seg_liver_supervision_1_short_connect_HED/seg_liver_supervision_1_short_connect_HED_binary'

d = []
e = []
a = natsort.natsorted(os.listdir(label_path))
b = natsort.natsorted(os.listdir(binary_path))

for i in range(len(a)):
    folders_dirs = os.path.join(label_path,a[i])
    folders_dirs_binary = os.path.join(binary_path,a[i])
    files = natsort.natsorted(os.listdir(folders_dirs))
    files_binary = natsort.natsorted(os.listdir(folders_dirs_binary))
#    print(files_binary)
    for j in range(len(files)):
        files_dirs = os.path.join(folders_dirs,files[j])
        files_binary_dirs = os.path.join(folders_dirs_binary,files[j])
        my_result_img = sitk.ReadImage(files_dirs)
        my_result_binary_img = sitk.ReadImage(files_binary_dirs)
#        print(files_dirs,files_binary_dirs)
        all_measure = sitk.LabelOverlapMeasuresImageFilter()
        all_measure.Execute(my_result_img,my_result_binary_img)
#        print(all_measure.GetDiceCoefficient())
        d.append(all_measure.GetDiceCoefficient())
#for z in range(len(d)):
#    if d[z]!=np.inf:
#        e.append(d[z])
#print(np.sum(e)/len(e))
for z in range(len(d)):
    if d[z] == np.inf:
        d[z] = 1.0      
print(np.sum(d)/len(d))

#for z in range(len(d)-1,-1,-1):
#    if d[z] == 0.0 or d[z] == np.inf:
#        d.pop(z)
#print(np.sum(d)/len(d))

#for z in range(len(d)):
#    if d[z] == 0.0:
#        d[z] = 1.0
#print(np.sum(d)/len(d))



