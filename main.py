import requests
from lxml import etree
#from bs4 import BeautifulSoup
#import bs4
# def getHtmlText(url):
#     try:
#         r=requests.get(url)
#         r.raise_for_status()
#         r.encoding=r.apparent_encoding
#         return r.text
#     except:
#         return "ERROR"
# def getMonthData(MonthList,html):
#     soup=BeautifulSoup(html,"html.parser")
#     for th in soup.find("th class").children:
#         if isinstance(th,bs4.element.Tag):
#             ths=th('Strong')
#             MonthList.append([ths[0].string,ths[1].string,ths[2].string]) 
def main():
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    req=requests.get(url)
    req.encoding="UTF-8"
    r=req.text
    tree=etree.HTML(r)
    nodes=tree.xpath("//tbody[@class='hidden_zhpm']/tr[@class='alt']/td/text()")
    i=0
    for node in nodes:
        print(node)
        i=i+1
        while(i>=10):
            print("\n")
            i=0
    #print(nodes)
    #print(r)
main()