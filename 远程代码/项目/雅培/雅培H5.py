#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路  %s,表示格化式一个对象为字符
# %d,整数

import pymssql, yaml, pandas, time
from selenium import webdriver

def liulan():
    r = webdriver.Firefox()
    r.get('https://abbotth5.wedochina.cn/question?useropenid=ol56vwyhceW-n7nlV63JktG0-dX4')
    return r
def wuliulan():
    req_url = "https://abbotth5.wedochina.cn/question?useropenid=ow_TXjhtigzmViZ4fcBLBAj0hxoI"
    c_options = webdriver.FirefoxOptions()
    # 设置chrome浏览器无界面模式
    c_options.add_argument('--headless')
    c_options.add_argument('--disable-gpu')
    browser = webdriver.Firefox(options=c_options)
    # 开始请求
    r=browser.get(req_url)
    return r
def shanchu(openid):
    d = yaml.load(open(r'D:\Caps.yaml'))
    con = pymssql.connect(host=d['yp_server'], port=d['yp_port'], user=d['yp_user'], password=str(d['yp_pwd']),
                          database=d['yp_db4'])
    cuesor = con.cursor()
    sql1 = "delete from JoinNumber where openid='%s'" % (openid)
    sql2 = "delete from LotteryRecord where userid='%s'" % (openid)
    sql3 = "delete from AnswerRecord where openid='%s'" % (openid)
    sql6 = "delete from Customer where openid='%s'" % (openid)
    sql5 = "delete  from RebirthCard where CustomerOpenId='%s' or CurrOpenId='%s'" % (openid,openid)
    sql4 = "update Customer set LotteryCount=0, Mobile='' where openid='%s'" % (openid)
    try:
        cuesor.execute(sql1)
        cuesor.execute(sql2)
        cuesor.execute(sql3)
        cuesor.execute(sql5)
        cuesor.execute(sql6)

        con.commit()
        return 'ok'
    except:
        con.rollback()
        return 'no'
    finally:
        cuesor.close()
        con.close()
def demo():
    r=liulan()
    time.sleep(2)
    d = r.find_element_by_css_selector("[class ='que-list auto']")
    for i in  range(1,13):
        print(i)
        weizhi="li:nth-child(%s)"%(i)
        dd=d.find_element_by_css_selector(weizhi)
        time.sleep(2)
        dd.find_element_by_css_selector("[dataisright ='true']").click()
        time.sleep(2)
    print(d)
# demo()
# 那路逗    ol56vw0RHmt_ryOuwWZtmlHaGQwg
# Polaris   ol56vwxTMwisjDZ80hx8HGqOtq1w
# 张綝 Sophia   ol56vw8nqowrwRYxfzMvE6MjTCus
# OPPOfindX😊   ol56vwyhceW-n7nlV63JktG0-dX4
# 沃家小编1234578979446   ol56vw9JT-DxDYYaZPdgcamFHTbo
print(shanchu('ol56vw0RHmt_ryOuwWZtmlHaGQwg'))

