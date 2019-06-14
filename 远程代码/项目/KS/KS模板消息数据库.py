#!/usr/bin/python
# -*- coding:utf8 -*-
import pymssql, yaml, pandas

d = yaml.load(open(r'D:\Caps.yaml'))

# con = pymssql.connect(host=server, port=3433, user=user, password=pwd, database='katespadewechat' )
# con = pymssql.connect(server=d['local_server'], user=d['local_user'], password=str(d['local_pwd']), database='test')
con = pymssql.connect(host=d['ks_server'],port=d['ks_prot'], user=d['test_user'], password=str(d['test_pwd']), database=d['ks_db'])

cuesor = con.cursor()
cuesor.execute(" select * from SmsRecord order by id desc")
row = cuesor.fetchall()

df=pandas.DataFrame(row)
df.to_csv(r'd:\短信.csv', encoding = 'utf-8')
print(row)
cuesor.close()
con.close()
