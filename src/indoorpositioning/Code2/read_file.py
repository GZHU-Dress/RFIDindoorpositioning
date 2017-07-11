# coding=utf-8

from reset_index import reset_index
from scipy import stats
import pandas as pd
import numpy as np
import random
import os
import re


def get_source_data(root_path):
    """获取源数据"""
    file_name = os.listdir(root_path)
    fdata = np.zeros((1, 6))
    for i in range(len(file_name)):
        fdata_tmp = read_file('%s' % root_path + file_name[i])
        [X_tmp, y_tmp] = read_loc(file_name[i])
        X = np.ones((len(fdata_tmp), 1)) * X_tmp
        y = np.ones((len(fdata_tmp), 1)) * y_tmp
        fdata_tmp = np.concatenate((fdata_tmp, X, y), axis=1)  # 横向拼接
        fdata = np.concatenate((fdata, fdata_tmp), axis=0)  # 纵向拼接
    fdata = np.delete(fdata, 0, 0)
    df = pd.DataFrame(fdata, columns=['id', 'rssi', 'times', 'ant', 'X', 'y'])
    df['rssi'] = df['rssi'].astype(float)
    df['times'] = df['times'].astype(float)
    df['ant'] = df['ant'].astype(float)
    df['X'] = df['X'].astype(float)
    df['y'] = df['y'].astype(float)
    df = unfold(df)
    return df


def get_Xtrain_data(df, X_all):
    """获得训练数据"""
    X_train_data = np.array([[1, 1, 1, 1, 1]])
    for X in X_all:
        X_data = df[df['X'] == X]
        X_data = X_data.drop(['X', 'y'], axis=1)
        ant_count = np.array([0])
        for ant_num in range(len(X_data.groupby(by='ant'))):
            ant_data_tmp = X_data[X_data['ant'] == ant_num + 1]
            ant_data_tmp = ant_data_tmp.drop(['ant'], axis=1)
            # ant_data_tmp = guass(ant_data_tmp)  # guass
            ant_count = np.append(ant_count, np.array([len(ant_data_tmp)]))
        ant_count = np.delete(ant_count, 0, 0)
        try:
            ant_count = ant_count.min()
            ant_data = np.ones((ant_count, 1))
        except ValueError:
            pass
        for ant_num in range(len(X_data.groupby(by='ant'))):
            ant_data_tmp = X_data[X_data['ant'] == ant_num + 1]
            ant_data_tmp = ant_data_tmp.drop(['ant'], axis=1)
            # ant_data_tmp = reset_index(ant_data_tmp)  # guass
            # ant_data_tmp = guass(ant_data_tmp)  # guass
            ant_data_tmp = reset_index(ant_data_tmp)
            if len(ant_data_tmp) != ant_count:
                drop_num = len(ant_data_tmp) - ant_count
                drop_labels = random.sample(
                    [n for n in range(len(ant_data_tmp))], drop_num)
                ant_data_tmp = ant_data_tmp.drop(drop_labels, axis=0)
            ant_data = np.concatenate((ant_data, ant_data_tmp), axis=1)
        ant_data = np.delete(ant_data, 0, 1)
        ant_data = np.concatenate(
            (ant_data, X * np.ones((len(ant_data), 1))), axis=1)
        X_train_data = np.concatenate((X_train_data, ant_data), axis=0)
    X_train_data = np.delete(X_train_data, 0, 0)
    return X_train_data


def get_ytrain_data(df, y_all):
    """获得训练数据"""
    y_train_data = np.array([[1, 1, 1, 1, 1]])
    for y in y_all:
        y_data = df[df['y'] == y]
        y_data = y_data.drop(['X', 'y'], axis=1)
        ant_count = np.array([0])
        for ant_num in range(len(y_data.groupby(by='ant'))):
            ant_data_tmp = y_data[y_data['ant'] == ant_num + 1]
            ant_count = np.append(ant_count, np.array([len(ant_data_tmp)]))
        ant_count = np.delete(ant_count, 0, 0)
        try:
            ant_count = ant_count.min()
            ant_data = np.ones((ant_count, 1))
        except ValueError:
            pass
        for ant_num in range(len(y_data.groupby(by='ant'))):
            ant_data_tmp = y_data[y_data['ant'] == ant_num + 1]
            ant_data_tmp = ant_data_tmp.drop(['ant'], axis=1)
            ant_data_tmp = reset_index(ant_data_tmp)
            if len(ant_data_tmp) != ant_count:
                drop_num = len(ant_data_tmp) - ant_count
                drop_labels = random.sample(
                    [n for n in range(len(ant_data_tmp))], drop_num)
                ant_data_tmp = ant_data_tmp.drop(drop_labels, axis=0)
            ant_data = np.concatenate((ant_data, ant_data_tmp), axis=1)
        ant_data = np.delete(ant_data, 0, 1)
        ant_data = np.concatenate(
            (ant_data, y * np.ones((len(ant_data), 1))), axis=1)
        y_train_data = np.concatenate((y_train_data, ant_data), axis=0)
    y_train_data = np.delete(y_train_data, 0, 0)
    return y_train_data


def read_file(path):
    """read the data file"""
    try:
        fp = open(path, 'r')
    except OSError:
        print("can't open this file")
    else:
        fdata = fp.readlines(2048)
        fp.close()
    for i in range(len(fdata)):
        fdata[i] = fdata[i].rstrip().split("   ")
    return fdata


def read_loc(path):
    coordinate = re.search(r'(\d\.\d|\d)-(\d\.\d|\d)', path)
    X = float(coordinate.group(1)) / 10
    y = float(coordinate.group(2)) / 10
    return X, y


def read_all_loc(root_path):
    file_name = os.listdir(root_path)
    X = np.array([])
    y = np.array([])
    for i in range(len(file_name)):
        [X_tmp, y_tmp] = read_loc(file_name[i])
        X = np.append(X, X_tmp)
        y = np.append(y, y_tmp)
    return X, y


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
    source_data = source_data.drop(['times'], axis=1)
    return source_data


def guass(ant_rssi_df):
    """
    数据的高斯处理
    """
    mu = ant_rssi_df.mean()  # 平均
    sigma = ant_rssi_df.std()  # 标准差
    if sigma['rssi'] == 0:  # 标准差=0 数据相等
        sigma['rssi'] = 0.00000000001
    f = stats.norm.pdf(ant_rssi_df, mu, sigma)  # 得到概率分布 返回ndarray
    f = pd.DataFrame(f, columns=['f'])  # 转DataFrame
    ant_rssi_f = pd.concat([ant_rssi_df, f], axis=1, join='inner')
    ant_rssi = ant_rssi_f[ant_rssi_f['f'] < 0.5]
    ant_rssi = ant_rssi.drop(['f'], axis=1)
    return ant_rssi


if __name__ == '__main__':
    root_path = '../Training_data/'
    df = get_source_data(root_path)
    print(df)
