#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路  %s,表示格化式一个对象为字符
# %d,整数

import pymssql, yaml, pandas

d = yaml.load(open(r'D:\Caps.yaml'))
con = pymssql.connect(host=d['yp_server'], port=d['yp_port'], user=d['yp_user'], password=str(d['yp_pwd']),
                      database=d['yp_db3'])
cuesor = con.cursor()

file = pandas.ExcelWriter(r'd:\a.xls')
def cs(shouji,sheet):
    # ！！！注意%s需要去掉引号，因为pymysql会自动为我们加上
    sql1="select * from Run_UserFriend  WHERE Inviter=%s"%(shouji)
    sql="select CreatorTime,ModifierTime,NickName FROM Customer WHERE id= '%s'",str(shouji)
    cuesor.execute(sql)
    row = cuesor.fetchall()
    for i in row:
        print(i[1])
    clom = []
    for i in cuesor.description:
        clom.append(i[0])
    f1 = pandas.DataFrame(row,index=None,columns=clom)
    f1.to_excel(excel_writer=file, sheet_name=str(sheet), encoding='utf-8')

for i in range (1,4):
    cs('ogb9a1FselRKRTlCdCe0N3qoRMXM',i)

file.save()
file.close()
print('ok')

cuesor.close()
con.close()
