#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:50:58 2019

@author: lty
"""


import SimpleITK as sitk
import numpy as np
import scipy.io
import natsort
import time
import os

start = time.time()
mat_array_path = '/media/lty/data/CRF_prepare/predict_img'
save_path = '/media/lty/data/CRF_prepare/predict_img'

folders = natsort.natsorted(os.listdir(mat_array_path))
for i in range(len(folders)):
    folders_path = os.path.join(mat_array_path, folders[i])
    files = natsort.natsorted(os.listdir(folders_path))
    
    volume = np.zeros((512,512,1))
    for j in range(len(files)):
        files_path = os.path.join(folders_path, files[j])
#        img = scipy.io.loadmat(files_path)['section']
        img = sitk.GetArrayFromImage(sitk.ReadImage(files_path))    ##images format .png
        volume = np.concatenate((volume,np.expand_dims(img,axis=-1)),axis=-1)
    volume = volume[:,:,1:]
    nii_image = sitk.GetImageFromArray(volume.transpose(2,0,1))
    sitk.WriteImage(nii_image,os.path.join(save_path,'test-segmentation-'+str(i))+'.nii')
    end = time.time()
    print(end-start)