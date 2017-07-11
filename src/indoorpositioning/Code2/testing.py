# coding=utf-8


from read_file import get_source_data
from read_file import read_all_loc
from reset_index import reset_index
import pandas as pd
import numpy as np
import random


def X_testing(theta):
    root_path = '../Forecast_data/'
    df = get_source_data(root_path)
    df = df[df['id'] == '00000007']
    df = df.drop(['id'], axis=1)
    [X_all, y_all] = read_all_loc(root_path)
    X_train_data = get_Xtrain_data(df, X_all)
    X_test_data = pd.DataFrame(X_train_data, columns=[
                               'ant0', 'ant1', 'ant2', 'ant3', 'X'])
    X_ones = np.ones((4, 1))
    test_data = np.ones((1, 5))
    for X in X_all:
        test_data_tmp = X_test_data[X_test_data['X'] == X]
        test_data_tmp = test_data_tmp.mean()
        test_data_tmp = test_data_tmp.as_matrix()
        test_data = np.append(test_data, [test_data_tmp], axis=0)
    test_data = np.delete(test_data, 0, 0)
    test_data = np.append(X_ones, test_data, axis=1)
    check_error = test_data[:, -1].reshape(4, 1)
    test_data = test_data[:, :5]
    result = np.dot(abs(test_data), theta / 10)
    error = abs(result - check_error)
    return error, result, test_data

def y_testing(theta):
    root_path = '../Forecast_data/'
    df = get_source_data(root_path)
    df = df[df['id'] == '00000007']
    df = df.drop(['id'], axis=1)
    [X_all, y_all] = read_all_loc(root_path)
    y_train_data = get_ytrain_data(df, y_all)
    y_test_data = pd.DataFrame(y_train_data, columns=[
                               'ant0', 'ant1', 'ant2', 'ant3', 'y'])
    y_ones = np.ones((4, 1))
    test_data = np.ones((1, 5))
    for y in y_all:
        test_data_tmp = y_test_data[y_test_data['y'] == y]
        test_data_tmp = test_data_tmp.mean()
        test_data_tmp = test_data_tmp.as_matrix()
        test_data = np.append(test_data, [test_data_tmp], axis=0)
    test_data = np.delete(test_data, 0, 0)
    test_data = np.append(y_ones, test_data, axis=1)
    check_error = test_data[:, -1].reshape(4, 1)
    test_data = test_data[:, :5]
    result = np.dot(abs(test_data), theta / 10)
    error = abs(result - check_error)
    return error, result, test_data

def X_testing_single(theta):
    root_path = '../Forecast_data/'
    df = get_source_data(root_path)
    df = df[df['id'] == '00000007']
    df = df.drop(['id'], axis=1)
    [X_all, y_all] = read_all_loc(root_path)
    X_train_data = get_Xtrain_data(df, X_all)
    X_test_data = pd.DataFrame(X_train_data, columns=[
                               'ant0', 'ant1', 'ant2', 'ant3', 'X'])
    test_data = np.ones((1, 5))
    for X in X_all:
        test_data_tmp = X_test_data[X_test_data['X'] == X]
        test_data_tmp = test_data_tmp.as_matrix()
        test_data = np.append(test_data, test_data_tmp, axis=0)
    test_data = np.delete(test_data, 0, 0)
    X_ones = np.ones((len(test_data), 1))
    test_data = np.append(X_ones, test_data, axis=1)
    check_error = test_data[:, -1].reshape(len(test_data), 1)
    test_data = test_data[:, :5]
    result = np.dot(abs(test_data), theta / 10)
    error = abs(result - check_error)
    return error, result, test_data

def y_testing_single(theta):
    root_path = '../Forecast_data/'
    df = get_source_data(root_path)
    df = df[df['id'] == '00000007']
    df = df.drop(['id'], axis=1)
    [X_all, y_all] = read_all_loc(root_path)
    y_train_data = get_ytrain_data(df, y_all)
    y_test_data = pd.DataFrame(y_train_data, columns=[
                               'ant0', 'ant1', 'ant2', 'ant3', 'y'])
    test_data = np.ones((1, 5))
    for y in y_all:
        test_data_tmp = y_test_data[y_test_data['y'] == y]
        test_data_tmp = test_data_tmp.as_matrix()
        test_data = np.append(test_data, test_data_tmp, axis=0)
    test_data = np.delete(test_data, 0, 0)
    y_ones = np.ones((len(test_data), 1))
    test_data = np.append(y_ones, test_data, axis=1)
    check_error = test_data[:, -1].reshape(len(test_data), 1)
    test_data = test_data[:, :5]
    result = np.dot(abs(test_data), theta / 10)
    error = abs(result - check_error)
    return error, result, test_data


def get_Xtrain_data(df, X_all):
    """获得训练数据"""
    X_train_data = np.array([[1, 1, 1, 1, 1]])
    for X in X_all:
        X_data = df[df['X'] == X]
        X_data = X_data.drop(['X', 'y'], axis=1)
        ant_count = np.array([0])
        for ant_num in range(len(X_data.groupby(by='ant'))):
            ant_data_tmp = X_data[X_data['ant'] == ant_num + 1]
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
