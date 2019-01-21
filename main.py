# -*- coding: utf-8 -*-
"""
Created on Thu Nov  25 14:00:51 2018

@author: YouminXUE

PartC. to predict the trend of BTCUSD by using the .csv file 
"""

import os
import time
import pandas as pd
from predict import predict
from SVM import SVM

rootdir = 'E:/python/stockdata/train'
list_doc = os.listdir(rootdir) #列出文件夹下所有的目录与文件

rootdir2 = 'E:/python/stockdata/test'
list_doc2 = os.listdir(rootdir2)

#define the root here
#windows
rootdir = 'C:/Users/Miku/Desktop/Coursework-YouminXUE-180864371/PartC/Gemini_BTCUSD_d.csv'
#centos
#rootdir = 'homes/yx305/Desktop/coursework/PartC/Gemini_BTCUSD_d.csv'

#load the data from the second line of csv
data = pd.read_csv("%s" %rootdir, header = 1)

path = []
path2 = []

accuracy = []
accuracy2 = []

length = []
acc_over_80 = []
stock_over_80 = []
acc_over_90 = []
stock_over_90 = []
time_start=time.time()


data_train = 
for i in range(0,len(list_doc)):
    lenth = os.path.join(rootdir,list_doc[i])
    lenth2 = os.path.join(rootdir2,list_doc[i])
    
    lenth = lenth.replace("\\", "/")
    lenth2 = lenth.replace("\\", "/")
    
    path.append(lenth)
    path2.append(lenth2)
    
    if os.path.isfile(path[i]):
        data_train = pd.read_csv("%s" %path[i], header = 0)#"%s"%path[i],  header = 0)
        data_test = pd.read_csv("%s" %path2[i], header = 0)
        try:
            score_train = SVM(data_train)[0]
            score_test = SVM(data_test)[0]
        except ValueError: 
            a = 1
        
        length.append(len(data_train))
        #print(list_doc[i], "的训练模型的精度为：", score)  
        accuracy.append(score_train)
        accuracy2.append(score_test)
    
for j in range(0,len(accuracy)):
    if (accuracy[j] >= 0.8) & (length[j] > 150) & (accuracy2[j] >=0.7):
        if (0.8 > accuracy[j]):
            acc_over_80.append(accuracy[j])
            stock_over_80.append(list_doc[j])
        else:
            acc_over_90.append(accuracy[j])
            stock_over_90.append(list_doc[j])
            
            
average = sum(accuracy)/len(accuracy)
print('\n\n\n精度大于90%的股票为：\n',stock_over_90)
print('精度在80%以上的股票为：\n',stock_over_80 )
print('\n\n该分类器的精度为', average)
time_end=time.time()
print('\n总共耗时：',time_end-time_start,'秒')

string = str(input("是否进行股票预测： Y / N\n"))
if (string == 'Y'):
    predict()
else:
    print("结束")