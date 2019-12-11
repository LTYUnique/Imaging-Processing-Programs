#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 09:13:16 2018

@author: lty
"""


import os 
import natsort

path = "/media/lty/data/3_liverseg-2017-nipsws-master/iterative_1" #文件夹目录 
a = []
files= natsort.natsorted(os.listdir(path)) #得到文件夹下的所有文件名称 
#print(files)
f1 = os.path.join(path,os.path.basename(files[0]))
#print(f1)
F = natsort.natsorted(os.listdir(f1))
#F.sort(key=lambda x:int(x[:]))
#print(F)
for i in range(len(F)):
    F1 = [os.path.join(files[0],F[i]),os.path.join(files[3],F[i]),os.path.join(files[4],F[i])]
    F1_2 = [os.path.join(files[1],F[i]),os.path.join(files[3],F[i]),os.path.join(files[4],F[i])] 
    F1_3 = [os.path.join(files[2],F[i]),os.path.join(files[3],F[i]),os.path.join(files[4],F[i])]
    print(F1,F1_2,F1_3)
    f2 = natsort.natsorted(os.listdir(os.path.join(path,F1[0])))
#    f2.sort(key=lambda x:int(x[:-4]))
    f2_2 = natsort.natsorted(os.listdir(os.path.join(path,F1_2[0])))
#    f2_2.sort(key=lambda x:int(x[:-4]))
    f2_3 = natsort.natsorted(os.listdir(os.path.join(path,F1_3[0])))
#    f2_3.sort(key=lambda x:int(x[:-4]))
#    print(f2_2)
    f3 = natsort.natsorted(os.listdir(os.path.join(path,F1[1])))
#    f3.sort(key=lambda x:int(x[:-4]))
    f3_2 = natsort.natsorted(os.listdir(os.path.join(path,F1_2[1])))
#    f3_2.sort(key=lambda x:int(x[:-4]))
    f3_3 = natsort.natsorted(os.listdir(os.path.join(path,F1_3[1])))
#    f3_3.sort(key=lambda x:int(x[:-4]))
#    print(f3_2)
    f4 = natsort.natsorted(os.listdir(os.path.join(path,F1[2])))
#    f4.sort(key=lambda x:int(x[:-4]))
    f4_2 = natsort.natsorted(os.listdir(os.path.join(path,F1_2[2])))
#    f4_2.sort(key=lambda x:int(x[:-4]))
    f4_3 = natsort.natsorted(os.listdir(os.path.join(path,F1_3[2])))
#    f4_3.sort(key=lambda x:int(x[:-4]))
#    #print(f4_2)
    for h in range(len(f2)):
        F2 = [os.path.join(F1[0],f2[h]),os.path.join(F1[1],f3[h]),os.path.join(F1[2],f4[h]),
              os.path.join(F1_2[0],f2_2[h]),os.path.join(F1_2[1],f3_2[h]),os.path.join(F1_2[2],f4_2[h]),
              os.path.join(F1_3[0],f2_3[h]),os.path.join(F1_3[1],f3_3[h]),os.path.join(F1_3[2],f4_3[h])]
#        F2_2 = [os.path.join(F1_2[0],f2_2[h]),os.path.join(F1_2[1],f3_2[h]),os.path.join(F1_2[2],f4_2[h])]
#        F2_3 = [os.path.join(F1_3[0],f2_3[h]),os.path.join(F1_3[1],f3_3[h]),os.path.join(F1_3[2],f4_3[h])]
#        print(F2)
        a.append(F2)
#        a.append(F2_2)
#        a.append(F2_3)

b = a
b.extend([])

for j in range(len(a)):
    c = b[j]  
    #print(c)
    with open('detector_path.txt', 'a') as final_file:                                
            for z in c:
                final_file.write(str(z))
                final_file.write(' ')
            final_file.write('\n') 