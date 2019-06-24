import requests
import re
from bs4 import BeautifulSoup
import pandas
from lxml import etree
from saveCSV import saveAsCSV
now_price = []
bookname = []
link = []
imglink = []
comnumber = []
cbs = []

price = []
comcount = []


def getHtmlText(url, key, pageNum):
    newurl = url+'key='+key+'&category_path=01.00.00.00.00.00&ddsale=1' + \
        '&page_index='+str(pageNum)
    try:
        r = requests.get(newurl)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "ERROR"


def main():
    key = input("请输入想要搜索书籍的关键字\n")
    url = 'http://search.dangdang.com/?'
    pageNum = 10
    for i in range(pageNum):
        html = getHtmlText(url, key, i)
        soup = BeautifulSoup(html, "lxml")
        tree = etree.HTML(html)
        bookname_set = soup.findAll("a", {"class": "pic"})
        link_set = soup.findAll("a", {"class": "pic"})
        now_price_set = soup.findAll("span", {"class": "search_now_price"})
        comnumber_set = soup.findAll("a", {"dd_name": "单品评论"})
        imglink_set = soup.findAll("a", {"dd_name": "单品图片"})
        cbs_set = soup.findAll("a", {"name": "P_cbs"})
        for a in bookname_set:
            bookname.append(a["title"])
        for a in link_set:
            link.append(a["href"])
        for span in comnumber_set:
            comcount.append(span.get_text())
        for span in now_price_set:
            price.append(span.get_text())
        for a in imglink_set:
            img = a.find("img")
            imglink.append(img['src'])
        for span in cbs_set:
            cbs.append(span.get_text())
    if len(cbs) < len(bookname):
        m = len(cbs)
        for i in range(len(bookname)-m):
            cbs.append("暂无数据")
    for i in price:
        i = re.sub(r'\u00A5', '', i)
        now_price.append(i)
    for i in comcount:
        i = re.sub(r'[\u4e00-\u9fa5]', '', i)
        comnumber.append(i)
    saveAsCSV(bookname, now_price, cbs, comnumber, link, imglink)
main()
