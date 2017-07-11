# coding=utf-8

from plt_X import plt_X
from reset_index import reset_index
import numpy as np
import random


def testing(train_data, distance, T, theta_summary):
    for ant_num in range(len(train_data.groupby(by='ant'))):
        testing_data = train_data[train_data['ant'] == ant_num + 1]
        testing_data = testing_data[testing_data['id'] == '00000007']
        testing_data = testing_data.drop(['ant', 'id'], axis=1)
        testing_data = reset_index(testing_data)
        testing_history = np.zeros((1, 1))
        testing_output_history = np.zeros((1, 1))
        for distance_num in distance:
            testing_rssi = testing_data[testing_data[
                'distance'] == distance_num[ant_num]]
            testing_output = distance_num[ant_num]
            testing_rssi = testing_rssi.drop(['distance'], axis=1)
            testing_rssi = reset_index(testing_rssi)
            if len(testing_rssi) % T != 0:
                drop_labels = len(testing_rssi) % T
                slice = random.sample(
                    [n for n in range(len(testing_rssi))], drop_labels)
                testing_rssi = testing_rssi.drop(slice, axis=0)
            testing_rssi = reset_index(testing_rssi)
            testing_rssi = testing_rssi.as_matrix().reshape((len(testing_rssi) // T), T)
            m = len(testing_rssi)
            testing_rssi = np.concatenate(
                (np.ones((m, 1)), testing_rssi), axis=1)
            testing_result_tmp = np.dot(abs(testing_rssi), theta_summary[
                                        :, ant_num:ant_num + 1] / 10)
            testing_result = np.array(
                [[testing_result_tmp.mean() - testing_output]])
            testing_output_history = np.concatenate((testing_output_history, np.array([[testing_output]])), axis=0)
            testing_history = np.concatenate((testing_history, testing_result), axis=0)
        testing_history = np.delete(testing_history, 0, 0)
        testing_output_history = np.delete(testing_output_history, 0, 0)
        error = np.concatenate(
            (abs(testing_history), testing_output_history), axis=1)
        plt_X(testing_history)
    return error
