import os
import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from saveCSV import getfilepath
lowprice = []
midprice = []
highprice = []
veryhighprice = []
Price = []
filepath = getfilepath()


def getPriceImg(filename):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = pd.read_csv(filename, usecols=['价格'])
        series = pd.Series(reader['价格'].values)
        for data in series:
            Price.append(data)
        for price in Price:
            if (price <= 50):
                lowprice.append(price)
            if (50 < price <= 100):
                midprice.append(price)
            if (100 < price <= 150):
                highprice.append(price)
            if(price > 150):
                veryhighprice.append(price)


getPriceImg(filepath)
labels = '<50', '50~100', '100~150', '>150'
sizes = [len(lowprice)/len(Price)*100, len(midprice)/len(Price)*100,
         len(highprice)/len(Price)*100, len(veryhighprice)/len(Price)*100]
explode = [0, 0.1, 0]
plt.pie(sizes, labels=labels, autopct='%1.1f %%', shadow=False, startangle=90)
plt.show()
