# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 14:36:30 2018

@author: Administrator
"""

import os
import numpy as np
from PIL import Image
import SimpleITK as sitk
import natsort

save_path = '/media/lty/data/333/masked_out_seg_lesion_supervision_1_original_final_nii'
original_path = '/media/lty/data/333/masked_out_seg_lesion_supervision_1_original_final'
original_folders = natsort.natsorted(os.listdir(original_path)) 
for i in range(len(original_folders)):
    original_folders_path = os.path.join(original_path,original_folders[i])
    files = natsort.natsorted(os.listdir(original_folders_path))

    all_list = []
    for j in range(len(files)):
        files_path = os.path.join(original_folders_path,files[j])
        files_array = np.array(Image.open(files_path))

        all_list.append(files_array)
        final_array = np.array(all_list)
        nii_image = sitk.GetImageFromArray(final_array)
#        sitk.WriteImage(nii_image,os.path.join(save_path,original_folders[i])+'.nii')
        sitk.WriteImage(nii_image,os.path.join(save_path,'test-segmentation-'+str(i))+'.nii')
print('done!')
