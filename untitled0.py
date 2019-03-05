# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 21:07:51 2019

@author: dell
"""

import numpy as np
import math as m
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

train_datasets = 10
test_datasets = 10000
a = 20
b = 0.2
c = 2 * m.pi
d = 2 #维度

#训练数据集
x = []
y = []
for i in range(train_datasets):
    xi = []
    yi = []
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(d):
        xii = np.random.uniform(-32.768, 32.768) 
        xi.append(xii)
        sum1 += xii ** 2
        sum2 += m.cos(c * xii)
        sum3 = -a * m.exp(-b * m.sqrt(sum1 / d)) - m.exp(sum2 / d) + a + m.exp(1)
    yi.append(sum3)    
    x.append(xi)
    y.append(yi)
print(y)