# coding=utf-8


import pandas as pd


def reset_index(X):
    tmps = pd.DataFrame({'rssi': [0]})
    X = X.append(tmps, ignore_index=True)
    X = X.drop((len(X) - 1), axis=0)
    return X
