# coding=utf-8

from read_file import get_source_data
from read_file import read_all_loc
from read_file import get_Xtrain_data
from read_file import get_ytrain_data
from testing import *
from training import training
import matplotlib.pyplot as plt


root_path = '../Training_data/'
df = get_source_data(root_path)
df = df[df['id'] == '00000007']
df = df.drop(['id'], axis=1)
[X_all, y_all] = read_all_loc(root_path)

X_train_data = get_Xtrain_data(df, X_all)
y_train_data = get_ytrain_data(df, y_all)
alpha = 0.01
num_iters = 400
T = 4
[X_theta, X_J_history] = training(X_train_data, T, alpha, num_iters)
plt.plot([p for p in range(len(X_J_history))], abs(X_J_history))
plt.show()
[y_theta, y_J_history] = training(y_train_data, T, alpha, num_iters)
plt.plot([p for p in range(len(y_J_history))], abs(y_J_history))
plt.show()

[X_error, X_result, X_test_data] = X_testing(X_theta)
plt.plot([p for p in range(len(X_error))], abs(X_error))
plt.show()

[X_test_error, X_result, X_test_data_beta] = X_testing_single(X_theta)
plt.plot([p for p in range(len(X_test_error))], abs(X_test_error))
plt.show()

[y_error, y_result, y_test_data] = y_testing(y_theta)
plt.plot([p for p in range(len(y_error))], abs(y_error))
plt.show()

[y_test_error, y_result, y_test_data_beta] = y_testing_single(y_theta)
plt.plot([p for p in range(len(y_test_error))], abs(y_test_error))
plt.show()
