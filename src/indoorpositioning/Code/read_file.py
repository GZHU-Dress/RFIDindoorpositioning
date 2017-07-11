#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:42:07 2017

@author: axionl
"""

import pandas as pd


def read_file(path):
    """读取文件"""
    try:
        fp = open(path, 'r')
    except OSError:
        print("can't open the file path")
    else:
        fdata = fp.readlines(2048)
        fp.close
    for i in range(len(fdata)):
        fdata[i] = fdata[i].rstrip().split("   ")
    df = pd.DataFrame(fdata, columns=['id', 'rssi', 'times', 'ant'])
    df['rssi'] = df['rssi'].astype(float)
    df['times'] = df['times'].astype(float)
    df['ant'] = df['ant'].astype(float)
    return df


if __name__ == "__main__":
    path = "../Sourcedata/2-2.txt"
    data = read_file(path)
    print("Data file has been read!")
