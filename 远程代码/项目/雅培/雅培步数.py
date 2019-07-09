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
    cuesor.execute("select * from Run_UserFriend  WHERE Inviter=%s " %shouji)
    row = cuesor.fetchall()
    for i in row:
        print(i[1])
    clom = []
    for i in cuesor.description:
        clom.append(i[0])
    f1 = pandas.DataFrame(row,columns=clom)
    f1.to_excel(excel_writer=file, sheet_name=str(sheet), encoding='utf-8')

for i in range (1,4):
    cs('ogb9a1OGFWkV1MdNddzLlAgq8iNQ',i)

file.save()
file.close()
print('ok')

cuesor.close()
con.close()
