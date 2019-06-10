#!/usr/bin/python
# -*- coding:utf8 -*-
import pymssql, yaml, logging

d = yaml.load(open(r'D:\Caps.yaml'))

# con = pymssql.connect(host=server, port=3433, user=user, password=pwd, database='katespadewechat' )
# con = pymssql.connect(server=d['local_server'], user=d['local_user'], password=str(d['local_pwd']), database='test')
con = pymssql.connect(host=d['ks_server'],port=d['ks_port'], user=d['ks_user'], password=str(d['ks_pwd']), database=d['ks_db'])

cuesor = con.cursor()
cuesor.execute(" SELECT top 1 * FROM [dbo].[WXFans]")
row = cuesor.fetchall()

print(row)
cuesor.close()
con.close()
