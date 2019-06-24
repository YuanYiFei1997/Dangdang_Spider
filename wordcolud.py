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
w = wordcloud.WordCloud(
    font_path=font,
    background_color='white',  # 背景色
    max_font_size=100,  # 设置最大字体
    width=800,
    height=1000,

)


def writeToTxt():
    filepath = getfilepath()
    load = pd.read_csv(filepath, usecols=['书籍名称'])
    serises = pd.Series(load['书籍名称'])
    return serises


# f = open('result.txt', "w+", encoding='utf-8')
# result = open("word.txt", 'r', encoding='utf-8')

# for line in result.readlines():
#     words = pseg.cut(line)
#     for w in words:
#         f.write(str(w)+" ")
f = open('result.txt', "r", encoding='utf-8')
i = str(re.sub(r'/[a-z]*', '', str(f.read())))
final = open('final.txt', "w+", encoding='utf-8')
final.write(i)
final.close()
fn=open('final.txt', "r", encoding='utf-8')
detail=fn.read()
w.generate(detail)
w = wordcloud.WordCloud()
w = wordcloud.WordCloud(collocations=False, font_path=font,
                        width=1400, height=1400, margin=2).generate(detail.lower())

plt.imshow(w)
plt.axis("off")
plt.show()
w.to_file("wordcloud.png")