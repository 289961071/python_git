#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
import pymssql, time

server = "192.168.1.40"
user = "lilu"
pwd = "Lilu329297!@#"

def select_sql_canshu(sql, canshu):
    if canshu == '' or sql == '':
        return 'no'
    else:
        try:
            con = pymssql.connect(server, user, pwd, 'KateSpadeWeChat')
            cuesor = con.cursor()
            ziduan = [canshu + '%']
            cuesor.execute(sql, (ziduan[0],))
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
            cuesor.close()
            con.close()


def insert_sql_canshu(sql,canshu):
    con = pymssql.connect(server, user, pwd, 'KateSpadeWeChat')
    # 接收返回值
    cuesor = con.cursor()
    ziduan = [canshu]
    if canshu == '':
        return 'no'
    else:
        try:
            cuesor.execute("insert INTO TEMP_ALL_V VALUES (%s, '13823285082', '小姐谈', '女',"
                           " NULL, NULL, '谈', '小姐', '2018-01-04', '深圳金光华', 61, 'SZ Kingglory', 'KSS75503', "
                           "'深圳金光华', 'KSS75503', N'', N'M', 6000.00, '2018-01-04', '2018-01-04', 1,  1000.00, "
                           "N'KSS75503', N'Lapsed', N'Lapsed', N'Handbag seeker', N'0R1H1S0J0S0T0F0L0O', NULL, NULL, "
                           "'2018-01-04 11:27:00.000', NULL, NULL, NULL, NULL, NULL, NULL, 2304.00, N'深圳金光华', 6000.00)",
                           (ziduan,))
            con.commit()
            return 'ok'
        except:
            con.rollback()
            return 'no'
        finally:
            con.close()


def upde_sql_canshu(sql,canshu):
    con = pymssql.connect(server, user, pwd, 'KateSpadeWeChat')
    # 接收返回值
    cuesor = con.cursor()
    ziduan = [canshu]
    if canshu == '':
        return 'no'
    else:
        try:
            cuesor.execute("DELETE FROM TEMP_ALL_V WHERE VIP_Mobile= %s", (ziduan,))
            con.commit()
            return 'ok'
        except:
            con.rollback()
            return 'no'
        finally:
            con.close()

# select_xiaofei('1778803')


