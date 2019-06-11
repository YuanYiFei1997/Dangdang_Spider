import requests
from bs4 import BeautifulSoup
import bs4
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
    url='http://data.stats.gov.cn/easyquery.htm?cn=E0104'
    req=requests.get(url)
    r=req.text
    soup=BeautifulSoup(r,"html.parser")
    print(soup.find_all("div"))
    #print(r)
main()