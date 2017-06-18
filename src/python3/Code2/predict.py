#!/usr/bin/env python
# coding=utf-8


from read_file import read_file
from read_file import unfold
from reset_index import reset_index
import numpy as np
import random
import pandas as pd
import os
import re

root_path = '../Source_data/'
file_name = os.listdir(root_path)
for i in range(len(file_name)):
    coordinate = re.search(r'\d*', file_name[i])
    mark = float(coordinate.group())
    fdata = read_file('%s' % root_path + file_name[i])
    df = pd.DataFrame(fdata, columns=['id', 'rssi', 'times', 'ant'])
    df['rssi'] = df['rssi'].astype(float)
    df['times'] = df['times'].astype(float)
    df['ant'] = df['ant'].astype(float)
    df = df[df['id'] == '00000007']
    df = df.drop(['id'], axis=1)
    df = reset_index(df)
    df = unfold(df)
    for ant_num in range(len(df.groupby(by='ant'))):
        ant_data_tmp = df[df['ant'] == ant_num + 1]
        ant_data_tmp = ant_data_tmp.drop(['ant'], axis=1)
