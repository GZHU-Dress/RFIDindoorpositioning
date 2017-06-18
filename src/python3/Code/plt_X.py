# coding=utf-8


import matplotlib.pyplot as plt


def plt_X(X):
    plt.plot([p for p in range(len(X))], abs(X))
    plt.show()
