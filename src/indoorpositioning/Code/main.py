#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:42:07 2017

@author: axionl
"""


from train_data import get_train_data
from training import training
from testing import testing
import numpy as np
import matplotlib.pyplot as plt

root_path = "../Training_data/"
[train_data, distance] = get_train_data(root_path)
alpha = 0.01  # 下降速度
num_iters = 300  # 迭代次数
training_summary = np.zeros((1, 6))
T = 5  # 矩阵行数

theta_summary = training(train_data, distance, T, alpha, num_iters)
# testing_result = testing(theta_summary)
error = testing(train_data, distance, T, theta_summary)
plt.plot(error[:, 1:2], error[:, 0:1], 'ro')
plt.show()
