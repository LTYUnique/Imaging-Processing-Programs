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
import natsort
path = '/media/lty/医学图像处理/病人数据/LITS-Challenge-Test-Data1/111' #文件夹目录 
files= natsort.natsorted(os.listdir(path))
f1 = os.path.join(path,os.path.basename(files[0]))
f2 = os.path.join(path,os.path.basename(files[1]))
F = natsort.natsorted((os.listdir(f1)))
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
        a = [a1,b1,c1,a2,b2,c2,a3,b3,c3]
#        print(a)
        with open('all_dataset_tseting_supervision_1.txt', 'a') as final_file:
            for z in a:
                final_file.write(str(z))
                final_file.write(' ')
            final_file.write('\n')
    
     
    
        
        
        
        
        
        
        

        
            
        
            
        


        
        
        
        