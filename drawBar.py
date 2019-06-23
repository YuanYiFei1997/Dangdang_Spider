import os
import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from saveCSV import getfilepath
font = {'family': 'SimHei',
        'weight': 'bold',
        'size': '16'}
plt.rc('font', **font)               # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)
filepath = getfilepath()
Commit = []
lowcommit = []
midcommit = []
highcommit = []
veryhighcommit = []


def getCommitImg(filename):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = pd.read_csv(filename, usecols=['评论数'])
        series = pd.Series(reader['评论数'].values)
        for i in series:
            Commit.append(i)
        for count in Commit:
            if (count <= 200):
                lowcommit.append(count)
            if (200 < count <= 1000):
                midcommit.append(count)
            if (1000 < count <= 3000):
                highcommit.append(count)
            if(count > 3000):
                veryhighcommit.append(count)

getCommitImg(filepath)
value = (len(lowcommit), len(midcommit), len(highcommit), len(veryhighcommit))
Commitlable = '<200', '200~1000', '1000~3000', '>3000'
plt.bar(Commitlable, value, 0.35, color='#87CEFA')
plt.xlabel('评论数量区间')
plt.ylabel('数量')
plt.show()
