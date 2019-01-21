# -*- coding: utf-8 -*-
"""
Created on Thu Nov  25 14:00:51 2018

@author: YouminXUE
"""


from sklearn import svm  


#3.15  数据更新
#百分比化


def SVM(data):
    
    dimension = len(data)
    
    data_x = data.loc[:,['ma5','ma10','ma20','v_ma5','v_ma10','turnover']].values
    data_y = data['label'].values.reshape(dimension,1)

    clf = svm.SVC(kernel='rbf', degree = 3, gamma='auto')
    fit_func = clf.fit(data_x, data_y) #data_y_label)
    score = fit_func.score(data_x, data_y) #data_y_label)
    return score, clf, data_x, data_y


#clf = svm.SVC(kernel='rbf', degree = 3, gamma='auto');该分类器的精度为 0.583952043477