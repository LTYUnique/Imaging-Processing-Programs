 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 09:42:51 2018

@author: lty
"""

import os
import natsort
import numpy as np
from PIL import Image
import cv2
import scipy.misc
from skimage import measure

result_path = '/media/lty/data/444/seg_liver_supervision_1_new_idea_no_change_loss_binary'
save_path = '/media/lty/data/444/seg_liver_supervision_1_new_idea_no_change_loss_opening'
#kernel = np.ones((9,9),np.uint8)  
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

#def RotateClockWise90(img):
#    trans_img = cv2.transpose( img )
#    new_img = cv2.flip(trans_img, 1)
#    return new_img

folders = natsort.natsorted(os.listdir(result_path))
for i in range(len(folders)):
    folders_dirs = os.path.join(result_path,folders[i])
    files = natsort.natsorted(os.listdir(folders_dirs))
    for j in range(len(files)):
        files_dirs = os.path.join(folders_dirs,files[j])
        img = Image.open(files_dirs)
        img_array = np.array(img)
        opening = cv2.morphologyEx(img_array, cv2.MORPH_OPEN, kernel)
#        opening = RotateClockWise90(opening)
#        label = measure.label(opening, 4)
        scipy.misc.imsave(os.path.join(save_path,folders[i])+'/'+files[j][0:-4]+'.png',opening)
        print('Done!')
