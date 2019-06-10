#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
import pymysql


def shujuku(name, mima):
    server = "localhost"
    user = "root"
    pwd = "123456"
    con = pymysql.connect(server, user, pwd, "lilu")
    # 接收返回值
    cuesor = con.cursor()
    ziduan = name
    cuesor.execute("SELECT count(*) FROM user1 WHERE `name`=%s and pwd =%s", (name,mima))
    row = cuesor.fetchall()[0][0]
    if row == 0:
        return 'no'
    else:
        return 'ok'


