#!/usr/bin/python
# coding=utf-8
import pymssql
server = "192.168.1.40"
user = "lilu"
pwd = "Lilu329297!@#"
con = pymssql.connect(host=server,port=3433,user=user,password=pwd,database='katespadewechat',)
con = pymssql.connect('localhost', 'sa', '123456','lilu')
# 接收返回值
cuesor = con.cursor()
ziduan=[8,'2ww','sss']
cuesor.execute("INSERT INTO user1  VALUES %s",(ziduan  ,))
# row = cuesor.fetchall()
con.commit()
# #打印字段名
# ziduan=[]
# for i in  cuesor.description:
#     print(i[0])
#     ziduan.append(i[0])
# print(len(cuesor.description))
# print(ziduan)
# #循环打印出对应的数据为list
# rows=[]
# for r in  row:
#     rows.append(r)
# f=pandas.DataFrame(rows,columns=ziduan)
# f.to_csv('d:/c.csv',mode='a')

# print(row)