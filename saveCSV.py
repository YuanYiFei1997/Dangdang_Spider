import pandas
import os


def saveAsCSV(bookname, now_price, cbs, comnumber, link, imglink):
    string = input("是否保存到CSV文件？Y/N")
    if string == 'Y'or string == 'y':
        merge = {"书籍名称": bookname,
                 "价格": now_price,
                 "出版社": cbs,
                 "评论数": comnumber,
                 "商品链接": link,
                 "图片链接": imglink}
        data = pandas.DataFrame(merge)
        string = input("请输入文件名")
        filepath = string+'.csv'
        filename = filepath
        try:
            data.to_csv(filepath, encoding='utf_8_sig')
            print("保存成功")
        except:
            print("保存失败，请检查数据或文件名")
    else:
        return


def getfilepath():
    csvlist = []
    filepath = 'D:\\'
    filelist = os.listdir(filepath)
    suffix = ".csv"
    iterlist = []
    k = 1
    for i in filelist:
        if suffix in i:
            csvlist.append(i)
    for i in csvlist:
        print(str(k)+":"+i)
        iterlist.append(k)
        k = k+1
    print("**************没有更多了**************")
    csvdict = dict(zip(iterlist, csvlist))
    choose = input("请选择一个文件:\n")
    finalpath = filepath+str(csvdict[int(choose)])
    return finalpath
