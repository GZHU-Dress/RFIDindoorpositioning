# coding=utf-8


from read_file import read_file
from reset_index import reset_index


import os
import re
import math
import numpy as np
import pandas as pd


def unfold(source_data):
    """将数据按照次数展开"""
    times_data = source_data['times']
    sum_new_data = pd.DataFrame()
    for n in range(len(times_data)):
        times = int(times_data.loc[n:n])
        i = 0
        new_data = pd.DataFrame()
        while i < (times - 1):
            new_data = pd.concat([new_data, pd.DataFrame.copy(
                source_data.loc[n:n, :])], ignore_index=True)
            i += 1
        sum_new_data = pd.concat([sum_new_data, new_data], ignore_index=True)
    source_data = pd.concat([source_data, sum_new_data], ignore_index=True)
    return source_data


def get_train_distance(root_path):
    """得到训练数据距离"""
    file_name = os.listdir(root_path)
    distance = []
    for i in range(len(file_name)):
        coordinate = re.search(r'(\d\.\d|\d)-(\d\.\d|\d)', file_name[i])
        X = float(coordinate.group(1)) / 10
        y = float(coordinate.group(2)) / 10
        distance_value = [math.sqrt((0 - X) ** 2 + (0 - y) ** 2), math.sqrt((1 - X) ** 2 + (
            0 - y) ** 2), math.sqrt((0 - X) ** 2 + (1 - y) ** 2), math.sqrt((1 - X) ** 2 + (1 - y) ** 2)]
        distance.append(distance_value)
    return distance


def get_train_data(root_path):
    distance = get_train_distance(root_path)
    file_name = os.listdir(root_path)
    train_data = pd.DataFrame(
        {'id': [], 'rssi': [], 'ant': [], 'distance': []})
    file_num = 0
    for path in file_name:
        source_data = read_file("../Training_data/%s" % path)
        unfold_data = unfold(source_data).drop(['times'], axis=1)
        for ant_num in range(4):
            train_tmp = unfold_data[unfold_data['ant'] == ant_num + 1]
            train_tmp = reset_index(train_tmp)
            distance_value = distance[file_num][
                ant_num] * np.ones((len(train_tmp), 1))
            distance_df = pd.DataFrame(distance_value, columns=['distance'])
            train_tmp = pd.DataFrame.join(train_tmp, distance_df)
            train_data = train_data.append(train_tmp, ignore_index=True)
        file_num += 1
    train_data = reset_index(train_data)
    return train_data, distance


if __name__ == '__main__':
    root_path = '../Training_data/'
    distance = get_train_distance(root_path)
    train_data = get_train_data(root_path, distance)
