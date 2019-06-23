import requests
import re
from bs4 import BeautifulSoup
import pandas
from saveCSV import saveAsCSV
now_price = []
bookname = []
link = []
imglink = []
comnumber=[]
cbs=[]

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
    url = 'http://search.dangdang.com/?'
    key = "python"
    pageNum = 10
    price=[]
    for i in range(pageNum):
        html = getHtmlText(url, key, i)
        soup = BeautifulSoup(html,"lxml")
        bookname_set=soup.findAll("a",{"class":"pic"})
        link_set=soup.findAll("a",{"class":"pic"})
        now_price_set=soup.findAll("span",{"class":"search_now_price"})
        comnumber_set=soup.findAll("a",{"dd_name":"单品评论"})
        imglink_set=soup.findAll("a",{"dd_name":"单品图片"})
        cbs_set=soup.findAll("a",{"name":"P_cbs"})
        for a in bookname_set:
            bookname.append(a["title"])
        for a in link_set:
            link.append(a["href"])
        for span in comnumber_set:
            comnumber.append(span.get_text())
        for span in now_price_set:
            now_price.append(span.get_text())
        for a in imglink_set:
            img=a.find("img")
            imglink.append(img["src"])
        for span in cbs_set:
            cbs.append(span.get_text())
    if len(cbs)<len(bookname):
        m=len(cbs)
        for i in range(len(bookname)-m):
            cbs.append("暂无数据")
    saveAsCSV(bookname,now_price,cbs,comnumber,link,imglink)

main()
