# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:37:16 2018

@author: Miku
"""

import os

rootdir = 'E:/python/stockdata/train'
list_doc = os.listdir(rootdir) #列出文件夹下所有的目录与文件

rootdir2 = 'E:/python/stockdata/test'
list_doc2 = os.listdir(rootdir2)

path = []

set1 = set(list_doc)
set2 = set(list_doc2)

dif = set1 ^ set2
diff = list(dif)
for i in range(0, len(diff)):   
    lenth = os.path.join(rootdir,diff[i])

    path.append(lenth)

for j in range(0, len(diff)):
    try:
        os.remove(path[j])
    except FileNotFoundError:
        print(path[j])
