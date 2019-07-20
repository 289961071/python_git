#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路  %s,表示格化式一个对象为字符
# %d,整数

import pymssql, yaml, pandas

d = yaml.load(open(r'D:\Caps.yaml'))
con = pymssql.connect(host=d['ks_server'], port=d['ks_port'], user=d['ks_user'], password=str(d['ks_pwd']),
                      database=d['ks_db'])
cuesor = con.cursor()

# file = pandas.ExcelWriter(r'd:\ksdemo.xls')
def cs(shouji):
    # ！！！注意%s需要去掉引号，因为pymysql会自动为我们加上，屁，得加上 sql直接写到execute里面 不要单独拿出来
    sql="select b.code,s.mobile from BusCoupon b, SysUserInfo s  where s.openid=b.openid and s.mobile='%s'",str(shouji)
    cuesor.execute(sql)
    row = cuesor.fetchall()
    for i in row:
        print(i[1])
    clom = []
    for i in cuesor.description:
        clom.append(i[0])
    f1 = pandas.DataFrame(row,index=None,columns=clom)
    # f1.to_excel(excel_writer=file, sheet_name='a',encoding='utf-8')
    f1.to_csv(r'd:\ksdemo.csv')
m={
"13418111510",
"13928872228",
"18520686885"
}
for i in m:
    cs('18520686885')
file.save()
file.close()
print('ok')
cuesor.close()
con.close()
