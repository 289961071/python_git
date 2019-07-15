#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路  %s,表示格化式一个对象为字符
# %d,整数

import pymssql, yaml, pandas

d = yaml.load(open(r'D:\Caps.yaml'))
con = pymssql.connect(host=d['ks_server'], port=d['ks_port'], user=d['ks_user'], password=str(d['ks_pwd']),
                      database=d['ks_db'])
cuesor = con.cursor()

file = pandas.ExcelWriter(r'd:\ks.xls')
def cs():
    # ！！！注意%s需要去掉引号，因为pymysql会自动为我们加上，屁，得加上
    sql="select  w.createtime,s.mobile from WXTemplateMsgSend w, sysuserinfo s where w.WXTemplateMsgInfoid=9 and" \
        " w.createtime > '2019-06-30 23:59:00' and w.FansOpenId=s.openid order by w.id"
    cuesor.execute(sql)
    row = cuesor.fetchall()
    for i in row:
        print(i[1])
    clom = []
    for i in cuesor.description:
        clom.append(i[0])
    f1 = pandas.DataFrame(row,index=None,columns=clom)
    f1.to_excel(excel_writer=file, sheet_name='七月_生日礼物领取提醒_人数', encoding='utf-8')

cs()
file.save()
file.close()
print('ok')

cuesor.close()
con.close()
