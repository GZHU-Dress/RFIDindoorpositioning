# -*- coding: utf-8 -*-
import numpy as np
import math


def getXY(xn, yn, dn):
    n = len(xn) - 1
    A = np.mat([2 * (xn - xn[n]), 2 * (yn - yn[n])]).T
    b = np.mat([np.square(xn) - np.square(xn[n]) + np.square(yn) - np.square(yn[n]) + np.square(dn[n]) - np.square(dn)]).T
    X = (A.T * A).I * A.T * b
    return X


if __name__ == '__main__':
    X = np.array([0, 0, 3, 3])
    Y = np.array([0, 3, 0, 3])
    d = np.array([math.sqrt(2), math.sqrt(5), math.sqrt(5), math.sqrt(8)])
    p = getXY(X, Y, d)
    print(p)