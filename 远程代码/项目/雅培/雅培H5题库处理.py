#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路  %s,表示格化式一个对象为字符
# %d,整数

import pymssql, yaml, pandas, time

def insert(val,leixing):
    d = yaml.load(open(r'D:\Caps.yaml'))
    con = pymssql.connect(host=d['local_server1'], user=d['local_user1'], password=str(d['local_pwd1']),
                          database=d['local_db1'])
    cuesor = con.cursor()
    sql0 = "select top 1 id from timu_tb  ORDER BY id desc"
    cuesor.execute(sql0)
    row=cuesor.fetchall()
    sql1 = "INSERT INTO timu_tb (timu,leixing)VALUES('%s','%s')" % (val[0],leixing)
    sql2 = "INSERT INTO daan_tb(daan,duicuo,timuid)  VALUES('%s',%d,%d)" % (val[1],0,row[0][0]+1)
    sql3 = "INSERT INTO daan_tb(daan,duicuo,timuid)  VALUES('%s',%d,%d)" % (val[2],0,row[0][0]+1)
    sql4 = "INSERT INTO daan_tb(daan,duicuo,timuid)  VALUES('%s',%d,%d)" % (val[3],1,row[0][0]+1)
    try:
        cuesor.execute(sql1)
        cuesor.execute(sql2)
        cuesor.execute(sql3)
        cuesor.execute(sql4)
        con.commit()
        return 'ok'
    except:
        con.rollback()
        return 'no'
    finally:
        cuesor.close()
        con.close()
def demo():
    f = pandas.read_excel(r'E:\LL\项目\31.雅培答题抽奖\答题H5题库0716.xlsx', sheet_name='产品')
    # print(f)
    df = pandas.DataFrame(f)
    # print(df[1:6])
    # print('index:',df[1:6].index)
    # print('columns:',df[1:6].columns)
    # print('values:',df[1:6].values)
    # a=df[1:6].values
    a=df.values
    c=0
    for i in a:
        c=c+1
        print(c,insert(i, '产品'))
demo()