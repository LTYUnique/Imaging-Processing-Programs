#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:23:06 2018

@author: xdg
"""
#第一步：解压原文件，到一个新的文件夹中
import zipfile
import os


path = '/home/yk/PETCT/data'#数据所在位置（改）
os.mkdir(os.path.join('/home/yk/PETCT','data_rp'))#新建文件夹data_rp（改：'/home/yk/PETCT'）
path1 = os.path.join('/home/yk/PETCT','data_rp')#data_rp的绝对路径（改）
for i in range(len(os.listdir(path))):
    folder = 'batch_%d' %(i+1)
    os.mkdir(os.path.join(path1,folder))#在data_rp下新建文件夹
    Old_folder = sorted(os.listdir(path))[i]
    New_folder = os.path.join(path1,folder)
    for filename in os.listdir(os.path.join(path,Old_folder)):
        Explode_file = os.path.join(os.path.join(path,Old_folder),filename)
        z = zipfile.ZipFile(Explode_file,'r') 
        z.extractall(New_folder)#将解压出来的文件夹放到指定的位置
        

  











