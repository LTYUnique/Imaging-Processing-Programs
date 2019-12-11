#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 17:14:36 2018

@author: lty
"""



'''filenames=os.listdir(dir)

    filenames.sort(key=lambda x:int(x[:-4]))#倒着数第四位'.'为分界线，按照‘.’左边的数字从小到大排序

    此时乱序就变成了顺序：filenames=['11.jpg' , '22.jpg' , '30.jpg']，即filenames[1]='22.jpg';当然可根据自己文件名的特征去决定int(x[:?])中？的
'''

import os 
import numpy as np
path = "/home/lty/LiTS_database" #文件夹目录 
a = []
files= os.listdir(path)
#print(files) 
f1 = os.path.join(path,os.path.basename(files[0]))
F = os.listdir(f1)
#print(F)
F.sort(key=lambda x:int(x[:]))
#print(F)
for i in range(len(F)):
    F1 = [os.path.join(files[0],F[i]),os.path.join(files[1],F[i]),os.path.join(files[2],F[i])]
    f2 = os.listdir(os.path.join(path,F1[0]))
    f2.sort(key=lambda x:int(x[:-4]))
#    f3 = os.listdir(os.path.join(path,F1[1]))
#    f3.sort(key=lambda x:int(x[:-4]))
#    f4 = os.listdir(os.path.join(path,F1[2]))
#    f4.sort(key=lambda x:int(x[:-4]))
    b = []
    for h in range(len(f2)):
#        F2 = [os.path.join(F1[0],f2[h]),os.path.join(F1[1],f3[h]),os.path.join(F1[2],f4[h])]
#        a.append(F2)
#        print(a)
        F2 = os.path.join(F1[0],f2[h])
        b = F2[h]+F2[h+1]+F2[h+2]
        print(b)
#for j in range(len(a)-2):
#    c = a[j]+a[j+1]+a[j+2]
#    #print(c)
#    with open('test_1.txt', 'a') as final_file:                                
#            for z in c:
#                final_file.write(str(z))
#                final_file.write(' ')
#            final_file.write('\n')        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#        a.append(F2)
#        #print(a)
        
#b = a
#
#b.extend([])
##b.append([])
##b.append([])
##b.append([])
##b.append([])
###print(b)
#for j in range(len(a)-3):
#    c = b[j]+b[j+1]+b[j+2]
#    #print(c)
#    with open('train_1.txt', 'a') as final_file:                                
#            for z in c:
#                final_file.write(str(z))
#                final_file.write(' ')
#            final_file.write('\n')   
        
            
        
            
        


        
        
        
        