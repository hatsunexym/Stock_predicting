# -*- coding: utf-8 -*-
"""
Created on Thu Nov  25 14:00:51 2018

@author: YouminXUE
"""
import pandas as pd
import os
import numpy as np  

from SVM import SVM
import matplotlib.pyplot as plt

def predict():
    rootdir = 'E:/python/stockdata/train'
    stock_num = os.path.join(rootdir,str(input("请输入想要预测的股票号码")) + '.csv')
    stock_path = stock_num.replace("\\", "/")
    if os.path.isfile(stock_path):
        data = pd.read_csv("%s" %stock_path, header = 0)#"%s"%path[i],  header = 0)

    acc = SVM(data)[0]
    print("此股票的预测精度为：", acc)
    
    in_close = float(input("请输入昨天的收盘价格"))
    in_ma5 = float(input("请输入昨天的5日均线"))
    in_ma10 = float(input("请输入昨天的10日均线"))
    in_ma20 = float(input("请输入昨天的20日均线"))
    in_volume = float(input("请输入昨天的成交量"))
    v_ma5 = float(input("请输入昨天的5日成交量"))
    v_ma10 = float(input("请输入昨天的10日成交量"))
    turnover = float(input("请输入昨天的流通量"))
    #v_ma20 = float(input("请输入昨天的20日成交量"))

    ma5 = (in_close - in_ma5)/in_ma5
    ma10 = (in_close - in_ma10)/in_ma10
    ma20 = (in_close - in_ma20)/in_ma20
    vma5 = (in_volume - v_ma5)/v_ma5
    vma10 = (in_volume - v_ma10)/v_ma10
    #vma20 = in_volume - v_ma20
    
#####是否进行标准化： preprocessing.scale()######
#    in_close = np.vstack((np.array(data['close'])[1::].reshape(dimension-1,1), in_close))
#    ma5 = np.vstack((np.array(data['ma5_trend'])[1::].reshape(dimension-1,1), ma5))
#    ma10 = np.vstack((np.array(data['ma10_trend'])[1::].reshape(dimension-1,1), ma10))
#    ma20 = np.vstack((np.array(data['ma20_trend'])[1::].reshape(dimension-1,1), ma20))   
#    in_close = preprocessing.scale(np.vstack((np.array(data['close'])[1::].reshape(dimension-1,1), in_close)))
#    ma5 = preprocessing.scale(np.vstack((np.array(data['ma5_trend'])[1::].reshape(dimension-1,1), ma5)))
#    ma10 = preprocessing.scale(np.vstack((np.array(data['ma10_trend'])[1::].reshape(dimension-1,1), ma10)))
#    ma20 = preprocessing.scale(np.vstack((np.array(data['ma20_trend'])[1::].reshape(dimension-1,1), ma20)))
#    in_volume = preprocessing.scale(np.vstack((np.array(data['volume'])[1::].reshape(dimension-1,1), in_volume)))
#    vma5 = preprocessing.scale(np.vstack((np.array(data['v_ma5_trend'])[1::].reshape(dimension-1,1), vma5)))
#    vma10 = preprocessing.scale(np.vstack((np.array(data['v_ma10_trend'])[1::].reshape(dimension-1,1), vma10)))
#    vma20 = preprocessing.scale(np.vstack((np.array(data['v_ma20_trend'])[1::].reshape(dimension-1,1), vma20)))
    
    x = np.hstack((ma5, ma10, ma20, vma5, vma10, turnover))#, vma20[-1]]
    x = x.reshape(1,6)
    #x = np.array(x).reshape(1,7) #vma20(1,8)
    clf = SVM(data)[1]  
    
    data_x = SVM(data)[2]
    data_y = SVM(data)[3]     

    pred = clf.predict(x) #若不需要进行标准化，则改为clf.predict(train_x)
    if pred < 0:
        print("预测今日为：跌", pred)
    else:
        print("预测今日为：涨", pred)
        
        
    #可视化
    plot_x = data['date'].values[0:20]
    plot_y = data_y[0:20]
    plt.scatter(data['date'].values[0:20], data_y[0:20], color='darkorange', label='data') 
    plt.hold('on')
    plt.plot([0,len(plot_x)],[0,0], '--', color = 'g')
    plt.plot(plot_x, plot_y, color='navy', lw=2, label='Origin model')    
    plt.plot(plot_x, clf.fit(data_x, data_y).predict(data_x)[0:20], color='cornflowerblue', lw=2, label='Linear model')  
    plt.xlabel('data')  
    plt.ylabel('target')  
    plt.title('SVM-Stock-Prediction')  
    plt.legend()  
    plt.show()
    
