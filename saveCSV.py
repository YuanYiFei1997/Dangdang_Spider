import pandas
def saveAsCSV(bookname,now_price,cbs,comnumber,link,imglink):
    string=input("是否保存到CSV文件？Y/N")
    if string=='Y':
        merge={"书籍名称":bookname,
        "价格":now_price,
        "出版社":cbs,
        "评论数":comnumber,
        "商品链接":link,
        "图片链接":imglink}
        data=pandas.DataFrame(merge)
        string=input("请输入文件名")
        filepath='D:\\'+string+'.csv'
        try:
            data.to_csv(filepath,encoding='utf_8_sig')
            print("保存成功")
        except:
            print("保存失败，请检查数据或文件名")
    else:
        return