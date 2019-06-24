import wordcloud
import pandas as pd
import jieba.analyse
from saveCSV import getfilepath
import jieba
import jieba.posseg as pseg
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import re
font = r'./font/simhei.ttf'


def getSerises():
    filepath = getfilepath()
    load = pd.read_csv(filepath, usecols=['书籍名称'])
    serises = pd.Series(load['书籍名称'])
    return serises


# 将原始数据写入word.txt
fw = open('TXT/word.txt', 'w+', encoding='utf-8')
fw.write(str(getSerises()))
fw.close()
word = open("TXT/word.txt", 'r', encoding='utf-8')
fr = open('TXT/result.txt', "w+", encoding='utf-8')
for line in word.readlines():
    words = pseg.cut(line)  # 将word.txt内的数据分段
    for w in words:
        fr.write(str(w)+" ")
fr.close()  # 关闭fr，解除对result.txt的占用
f = open('TXT/result.txt', "r", encoding='utf-8')
i = str(re.sub(r'/[a-z]*', '', f.read()))  # 利用正则表达式清洗掉文件中的分隔符 如/m，/eng等
final = open('TXT/final.txt', "w+", encoding='utf-8')
final.write(i)
final.close()
fn = open('TXT/final.txt', "r", encoding='utf-8')
detail = fn.read()
w = wordcloud.WordCloud()
w.generate(detail)
w = wordcloud.WordCloud(collocations=False, font_path=font, background_color='#000000',
                        width=1400, height=1400, margin=2).generate(detail.lower())

plt.imshow(w)
plt.axis("off")
plt.show()
text = input("请输入保存文件名")
string = './WordCloudImg/'+text+'.png'
w.to_file(string)
print("保存成功")
fn.close
