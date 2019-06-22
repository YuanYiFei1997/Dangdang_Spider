import requests
from lxml import etree
import pymysql
import re
def connect_DB():
    return pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='',
        database='db_spider'
    )

def getHtmlText(url, key , pageNum):
    # kv = {"key": key}
    newurl=url+'key='+key+'&category_path=01.00.00.00.00.00&ddsale=1'+'&page_index='+str(pageNum)
    try:
        r = requests.get(newurl)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "ERROR"
def main():
    url = 'http://search.dangdang.com/?'
    key = "python"
    pageNum=10
    for i in range(10):
        html=getHtmlText(url,key,i)
        tree = etree.HTML(html)
        bookname = tree.xpath('//ul[@class="bigimg"]/li[starts-with(@class,"line")]/a/@title')
        nowprice=tree.xpath('//ul[@class="bigimg"]/li[starts-with(@class,"line")]/p[@class="price"]/span[@class="search_now_price"]/text()')
        preprice=tree.xpath('//ul[@class="bigimg"]/li[starts-with(@class,"line")]/p[@class="price"]/span[@class="search_pre_price"]/text()')
        pubHouseName=tree.xpath('//ul[@class="bigimg"]/li[starts-with(@class,"line")]/p[@class="search_book_author"]/span/a[@name="P_cbs"]/text()')

main()