#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:00:49 2019

@author: lty
"""

import os 
import natsort

path = "/media/lty/data/3_liverseg-2017-nipsws-master/iterative_11" #文件夹目录 
a = []
files= natsort.natsorted(os.listdir(path)) #得到文件夹下的所有文件名称 
#print(files)
f1 = os.path.join(path,os.path.basename(files[0]))
#print(f1)
F = natsort.natsorted(os.listdir(f1))
#print(F)
for i in range(len(F)):
    F1 = [os.path.join(files[0],F[i]),os.path.join(files[2],F[i]),os.path.join(files[1],F[i]),os.path.join(files[4],F[i])]
    F1_2 = [os.path.join(files[0],F[i]),os.path.join(files[2],F[i]),os.path.join(files[1],F[i]),os.path.join(files[4],F[i])] 
    F1_3 = [os.path.join(files[5],F[i]),os.path.join(files[2],F[i]),os.path.join(files[1],F[i]),os.path.join(files[4],F[i])]
#    print(F1,F1_2,F1_3)

    f2 = natsort.natsorted(os.listdir(os.path.join(path,F1[0])))
    f2_2 = natsort.natsorted(os.listdir(os.path.join(path,F1_2[0])))
    f2_3 = natsort.natsorted(os.listdir(os.path.join(path,F1_3[0])))
#    print(F1[0],F1_2[0],F1_3[0])
    f3 = natsort.natsorted(os.listdir(os.path.join(path,F1[1])))
    f3_2 = natsort.natsorted(os.listdir(os.path.join(path,F1_2[1])))
    f3_3 = natsort.natsorted(os.listdir(os.path.join(path,F1_3[1])))
#    print(F1[1],F1_2[1],F1_3[1])
    f4 = natsort.natsorted(os.listdir(os.path.join(path,F1[2])))
    f4_2 = natsort.natsorted(os.listdir(os.path.join(path,F1_2[2])))
    f4_3 = natsort.natsorted(os.listdir(os.path.join(path,F1_3[2])))
#    print(F1[2],F1_2[2],F1_3[2])
    f5 = natsort.natsorted(os.listdir(os.path.join(path,F1[3])))
    f5_2 = natsort.natsorted(os.listdir(os.path.join(path,F1_2[3])))
    f5_3 = natsort.natsorted(os.listdir(os.path.join(path,F1_3[3])))
#    print(F1[3],F1_2[3],F1_3[3])
    for h in range(len(f2)):
        F2 = [os.path.join(F1[0],f2[h]),os.path.join(F1[1],f3[h]),os.path.join(F1[2],f4[h]),os.path.join(F1[3],f5[h]),
              os.path.join(F1_2[0],f2_2[h]),os.path.join(F1_2[1],f3_2[h]),os.path.join(F1_2[2],f4_2[h]),os.path.join(F1_2[3],f5_2[h]),
              os.path.join(F1_3[0],f2_3[h]),os.path.join(F1_3[1],f3_3[h]),os.path.join(F1_3[2],f4_3[h]),os.path.join(F1_3[3],f5_3[h])]
#        print(F2)
        a.append(F2)
        
b = a
b.extend([])

for j in range(len(a)):
    c = b[j]  
    #print(c)
    with open('seg_lesion_iterative_1_change_val.txt', 'a') as final_file:                                
            for z in c:
                final_file.write(str(z))
                final_file.write(' ')
            final_file.write('\n') 