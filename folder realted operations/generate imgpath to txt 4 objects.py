#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:43:40 2019

@author: lty
"""

import os
import natsort
path = '/media/lty/办公/liverseg-2017-nipsws-master/results_all_database/111' #文件夹目录 
files= natsort.natsorted(os.listdir(path))
f1 = os.path.join(path,os.path.basename(files[0]))
f2 = os.path.join(path,os.path.basename(files[1]))
F = natsort.natsorted((os.listdir(f1)))
#print(files)
for file in F:
    path_num = os.path.join(f1, file)
    aim_file = natsort.natsorted(os.listdir(path_num))
    path_num_1 = os.path.join(f2,file)
    aim_file_1 = natsort.natsorted(os.listdir(path_num_1))
    aim_file.sort(key=lambda x:int(x[:-4]))
    for i in range(len(aim_file)-2):
        a1 = os.path.join(files[0],file,aim_file[i])
        a2 = os.path.join(files[0],file,aim_file[i + 1])
        a3 = os.path.join(files[0],file,aim_file[i + 2])
        b1 = os.path.join(files[1],file,aim_file_1[i])
        b2 = os.path.join(files[1],file,aim_file_1[i + 1])
        b3 = os.path.join(files[1],file,aim_file_1[i + 2])
        c1 = os.path.join(files[2],file,aim_file_1[i])
        c2 = os.path.join(files[2],file,aim_file_1[i + 1])
        c3 = os.path.join(files[2],file,aim_file_1[i + 2])
        d1 = os.path.join(files[3],file,aim_file_1[i])
        d2 = os.path.join(files[3],file,aim_file_1[i + 1])
        d3 = os.path.join(files[3],file,aim_file_1[i + 2])
        a = [a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3]
#        print(a)
        with open('testing_lesion_commonbb_nobackprop_3_0_69.txt', 'a') as final_file:
            for z in a:
                final_file.write(str(z))
                final_file.write(' ')
            final_file.write('\n')