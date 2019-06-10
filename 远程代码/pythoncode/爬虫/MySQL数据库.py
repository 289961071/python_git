#!/usr/bin/python
# coding=utf-8
import pymysql,pandas

server = "localhost"
user = "root"
pwd = "123456"
con = pymysql.connect(server, user, pwd, "lilu")
# 接收返回值
cuesor = con.cursor()
ziduan=[9,'dsds','dsds2']
row=cuesor.execute("INSERT into user1  (id,name,pwd) VALUES %s",(ziduan ,) )
# row = cuesor.fetchall()
con.commit()
#打印字段名
ziduan=[]
for i in  cuesor.description:
    print(i[0])
    ziduan.append(i[0])
print(len(cuesor.description))
print(ziduan)
#循环打印出对应的数据为list
rows=[]
for r in  row:
    rows.append(r)
f=pandas.DataFrame(rows,columns=ziduan)
f.to_csv('d:/c.csv',mode='a')

print(row)
