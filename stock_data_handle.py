# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 09:08:39 2018

@author: Miku
"""
import pandas as pd
import numpy as np
import os

def SVM(data):
    dimension = len(data)
    
    stock_close = pd.DataFrame(data, columns = ['close'])
    price_change = pd.DataFrame(data, columns = ['price_change'])
    daily_normal = price_change.values
    
    for j in range(0,dimension - 1):
        if daily_normal[j] >= 0:
            daily_normal[j] = 1
        else:
            daily_normal[j] = -1
            
    close = data['close'].values      #X
    
    #五日均线涨跌情况
    stock_ma5 = pd.DataFrame(data, columns = ['ma5'])
    #ma5_trend = stock_close.values - stock_ma5.values
    data['ma5_trend'] = (stock_close.values - stock_ma5.values)/ stock_ma5.values
    ma5 = data['ma5_trend'].values
    #是否进行标准化：ma5 = preprocessing.scale(np.array(data['ma5_trend'])[1::])
    
    
    
    #十日均线涨跌情况
    stock_ma10 = pd.DataFrame(data, columns = ['ma10'])
    data['ma10_trend'] = (stock_close.values - stock_ma10.values)/stock_ma10.values
    ma10 = data['ma10_trend'].values
    #是否进行标准化：ma10 = preprocessing.scale(np.array(data['ma10_trend'])[1::])
    
    
    
    #二十日均线涨跌情况
    stock_ma20 = pd.DataFrame(data, columns = ['ma20'])
    data['ma20_trend'] = (stock_close.values - stock_ma20.values)/stock_ma20.values
    ma20 = data['ma20_trend'].values
    #是否进行标准化：ma20 = preprocessing.scale(np.array(data['ma20_trend'])[1::])
    ########################################################################
    
    #成交量标准化处理
    data['volume'] = pd.DataFrame(data, columns = ['volume'])
    volume_normal  = data['volume'].values
    #是否进行标准化：volume_normal = preprocessing.scale(np.array(data['volume'])[1::])
    
    #五日成交量情况
    v_ma5 = pd.DataFrame(data, columns = ['v_ma5'])
    data['v_ma5_trend'] = (data['volume'].values.reshape(dimension,1) - v_ma5.values)/v_ma5.values
    v_ma5 = data['v_ma5_trend'].values
    #是否进行标准化：v_ma5 = preprocessing.scale(np.array(data['v_ma5_trend'])[1::])
    
    
    #十日成交量情况
    v_ma10 = pd.DataFrame(data, columns = ['v_ma10'])
    data['v_ma10_trend'] = (data['volume'].values.reshape(dimension,1) - v_ma10.values)/v_ma10.values
    v_ma10 = data['v_ma10_trend'].values
    #是否进行标准化：v_ma10 = preprocessing.scale(np.array(data['v_ma10_trend'])[1::])
    
    #二十日成交量情况
    #v_ma20 = pd.DataFrame(data, columns = ['v_ma20'])
    #data['v_ma20_trend'] = data['volume'].values.reshape(dimension,1) - v_ma20.values
    #v_ma20 = preprocessing.scale(np.array(data['v_ma20_trend'])[1::])
    
    
    ########################################################################
    # 特征集合
    #X_train_minmax = min_max_scaler.fit_transform(X_train)
    #close = preprocessing.scale(close)
    date = pd.DataFrame(data['date'].values[1:dimension])
    data_X = pd.DataFrame({"close":close[1:dimension]})
    data_X.insert(0, 'date', date)
    
    data_X['volume'] = pd.DataFrame(np.array(volume_normal)[1:dimension])
    data_X['ma5'] = pd.DataFrame(np.array(ma5)[1:dimension]) 
    data_X['ma10'] = pd.DataFrame(np.array(ma10)[1:dimension]) 
    data_X['ma20'] = pd.DataFrame(np.array(ma20)[1:dimension]) 
    data_X['v_ma5'] = pd.DataFrame(np.array(v_ma5)[1:dimension]) 
    data_X['v_ma10'] = pd.DataFrame(np.array(v_ma10)[1:dimension])#,'ma20']]
    data_X['turnover'] = pd.DataFrame(data['turnover'].values[1:dimension])
    data_X['label'] = pd.DataFrame(np.array(daily_normal)[0:dimension-1])
    return data_X



rootdir = 'E:/python/stock'
list_doc = os.listdir(rootdir) #列出文件夹下所有的目录与文件
path = []
a = 0
length = []
for i in range(0,len(list_doc)):
    lenth = os.path.join(rootdir,list_doc[i])
    lenth = lenth.replace("\\", "/")
    path.append(lenth)
    if os.path.isfile(path[i]):
        data = pd.read_csv("%s" %path[i], header = 0)#"%s"%path[i],  header = 0)
        try:
            SVM(data).to_csv('%s' %list_doc[i])
        except ValueError:
            a += 1
        else:
            a +=0
        #print(list_doc[i], "的训练模型的精度为：", score)  
