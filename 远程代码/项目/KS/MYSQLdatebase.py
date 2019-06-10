#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
import pymysql, time

server = "localhost"
user = "root"
pwd = "123456"


def select_sql_canshu(sql, canshu1, canshu2):
    if canshu2 == '' or canshu1 == '' or sql == '':
        return 'no'
    else:
        try:
            con = pymysql.connect(server, user, pwd, "lilu")
            cuesor = con.cursor()
            ziduan = [canshu1, canshu2]
            cuesor.execute(sql, (ziduan[0], ziduan[1]))
            row = cuesor.fetchall()
            # #打印字段名
            clom = []
            for i in cuesor.description:
                clom.append(i[0])
            count = len(row)
            if count == 0:
                return 'no'
            else:
                p = {'r': list(row), 'c': clom, 'd': count}
                return p
        except:
            return 'no'
        finally:
            con.close()


def gai_sql_canshu(sql, canshu1, canshu2):
    con = pymysql.connect(server, user, pwd, "lilu")
    # 接收返回值
    cuesor = con.cursor()
    ziduan = [canshu1, canshu2]
    if canshu1 == '' or canshu2 == '':
        return 'no'
    else:
        try:
            cuesor.execute(sql, (ziduan[0], ziduan[1]))
            con.commit()
            return 'ok'
        except:
            con.rollback()
            return 'no'
        finally:
            con.close()


# sql2 =   sql3='CALL select_by_canshu( %s, %s)'
# b = select_sql_canshu(sql2, '111', '111')
# print(b)
