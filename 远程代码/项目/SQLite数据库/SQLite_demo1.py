# coding=utf-8
# 李路  python3.6以上自带的数据库SQLite  位置在本项目位置

import sqlite3

def sqlite1():
    con=sqlite3.connect('test.db')
    curso=con.cursor()
    curso.execute('select * from user')
    row=curso.fetchall()
    print(row)
    curso.close()
    con.commit()
    con.close()
sqlite1()