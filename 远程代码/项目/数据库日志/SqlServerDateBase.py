#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
import pymssql, time

server = "localhost"
user = "sa"
pwd = "123456"


def select_sql_canshu(sql, canshu1, canshu2):
    if canshu2 == '' or canshu1 == '' or sql == '':
        return 'no'
    else:
        con = pymssql.connect(server, user, pwd, "lilu")
        try:
            cuesor = con.cursor()
            ziduan = [canshu1, canshu2]
            cuesor.execute(sql, (ziduan[0], ziduan[1]))
            con.commit()
            row = cuesor.fetchall()
            # #打印字段名
            print(row)
            clom = []
            for i in cuesor.description:
                clom.append(i[0])
            count = len(row)
            if count == 1 and row[0][0]==None:
                return 'no'
            else:
                p = {'zhi': list(row), 'lie': clom, 'tiao': count}
                return p
        except:
            return 'no'
        finally:
            con.close()


sql1 = 'EXEC update_by_power %s,%s '
sql2 = 'select * from user_login where zhanghao=%s and pwd=%s '
a= select_sql_canshu(sql1,'ll','ll')
print(a)
