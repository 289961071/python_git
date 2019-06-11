# coding=utf-8
# 李路
import requests,datetime,pandas
from lxml import etree
from bs4 import BeautifulSoup
#B站的弹幕文件在 源码的 cID 里 75163572
url='https://comment.bilibili.com/75163572.xml'
r=requests.get(url)
r.encoding='utf-8'

#解析页面
#lxml是常用的解析器，需要提前使用pip工具安装lxml库
soup=BeautifulSoup(r.text,'lxml')
d=soup.find_all('d') #找到所有页面的d标签
# print(d[:10])

#给到CVS
dl=[]
n=0
for i in d:
    n+=1
    danmu={}
    danmu['弹幕']=i.text
    danmu['网址']=url
    danmu['时间']=datetime.date.today()
    dl.append(danmu)
print('获取了 %s 条' %n)

df=pandas.DataFrame(dl)
df.to_csv(r'd:\b站弹幕.csv')