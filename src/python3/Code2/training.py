# coding=utf-8


import numpy as np


def training(train_data, T, alpha, num_iters):
    [theta, J_history] = machine_learning(abs(train_data[:, :T]), train_data[
                                          :, T:T + 1], alpha, num_iters)
    return theta, J_history


def machine_learning(X, y, alpha, num_iters):
    m = len(y)
    x0 = np.ones((m, 1))
    X = featureNormalize(X)
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
    return X_norm


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
