import requests
from bs4 import BeautifulSoup
import bs4


def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "ERROR"

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivList(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校","总分"))
    for i in range(num):
         u=ulist[i]
         print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHtmlText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 20 univs

main()
