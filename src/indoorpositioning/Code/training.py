# coding=utf-8

from plt_X import plt_X
from reset_index import reset_index
import numpy as np
import random


def training(train_data, distance, T, alpha, num_iters):
    theta_summary = np.ones((T + 1, 1))
    training_summary = np.zeros((1, T + 1))
    for ant_num in range(len(train_data.groupby(by='ant'))):
        training_data = train_data[train_data['ant'] == ant_num + 1]
        training_data = training_data[training_data['id'] == '00000007']
        training_input = training_data.drop(['ant', 'id'], axis=1)
        training_input = reset_index(training_input)
        for distance_num in distance:
            training_rssi = training_input[
                training_input['distance'] == distance_num[ant_num]]
            training_rssi = training_rssi.drop(['distance'], axis=1)
            training_rssi = reset_index(training_rssi)
            if len(training_rssi) % T != 0:
                drop_labels = len(training_rssi) % T
                slice = random.sample(
                    [n for n in range(len(training_rssi))], drop_labels)
                training_rssi = training_rssi.drop(slice, axis=0)
            training_rssi = reset_index(training_rssi)
            training_rssi = training_rssi.as_matrix().reshape((len(training_rssi) // T), T)
            m = len(training_rssi)
            training_output = distance_num[ant_num] * np.ones((m, 1))
            training_summary_tmp = np.concatenate(
                (training_rssi, training_output), axis=1)
            training_summary = np.concatenate(
                (training_summary, training_summary_tmp), axis=0)
        training_summary = np.delete(training_summary, 0, 0)
        training_summary_num = len(training_summary) // 10 * 6
        [theta, J_history] = machine_learning(
            abs(training_summary[:training_summary_num, 0:T]), training_summary[:training_summary_num, T:T + 1], alpha, num_iters)
        plt_X(J_history)
        theta_summary = np.concatenate((theta_summary, theta), axis=1)
    theta_summary = np.delete(theta_summary, 0, 1)
    return theta_summary


def machine_learning(X, y, alpha, num_iters):
    m = len(y)
    x0 = np.ones((m, 1))
    [X, mu, sigma] = featureNormalize(X)
    X = np.concatenate((x0, X), axis=1)
    theta = np.zeros((np.shape(X)[1], 1))
    [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
    return theta, J_history


def featureNormalize(X):
    X_norm = X
    mu = np.mean(X, axis=0)
    sigma = np.std(X, ddof=1, axis=0)
    for n in range(len(sigma)):
        if sigma[n] == 0:
            sigma[n] = 0.0001
    for i in range(np.shape(X)[1]):
        X_norm[:, i:i + 1] = (X[:, i:i + 1] - mu[i]) / sigma[i]
    return X_norm, mu, sigma


def gradientDescentMulti(X, y, theta, alpha, num_iters):
    m = len(y)
    J_history = np.zeros((num_iters, 1))
    for iter in range(num_iters):
        htheta = np.dot(X, theta)
        theta_tmp = np.zeros((np.shape(X)[1], 1))
        for row in range(np.shape(theta)[0]):
            theta_tmp[row] = theta[row] - alpha / m * \
                np.sum((htheta - y) * X[:, row:row + 1])
        theta = theta_tmp
        J_history[iter] = computeCostMulti(X, y, theta)
    return theta, J_history


def computeCostMulti(X, y, theta):
    m = len(y)
    J = 0
    J = np.dot((np.dot(X, theta) - y).T, (np.dot(X, theta) - y)) / (2 * m)
    return J
