import requests
from bs4 import BeautifulSoup
def getHtmlText(url, key):
    try:
        kv={"key":key}
        r = requests.get(url, params=kv)
        r.raise_for_status()  # 如果状态码为200则不抛异常，反之则抛出异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "ERROR"
key="python"
url = 'http://search.dangdang.com/?'
gethtml=getHtmlText(url,key)
num=1
while(num<=60):
    count="line"+str(num)
    num=num+1
    soup = BeautifulSoup(gethtml,"html.parser")
    tags=soup.find_all(class_=count)
    for tag in tags:
        print (tag.a['title'])