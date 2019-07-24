#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路  %s,表示格化式一个对象为字符
# %d,整数

import pymssql, yaml, pandas, time
from selenium import webdriver

def liulan():
    r = webdriver.Firefox()
    r.get('https://abbotth5.wedochina.cn/question?useropenid=ol56vw3R6dFqT74HAUoKkfEBfkuE')
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
    try:
        cuesor.execute(sql1)
        cuesor.execute(sql2)
        cuesor.execute(sql3)

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
    d = r.find_element_by_css_selector("[class ='que-list auto ta-c']")
    for i in  range(1,13):
        print(i)
        weizhi="li:nth-child(%s)"%(i)
        dd=d.find_element_by_css_selector(weizhi)
        time.sleep(1)
        dd.find_element_by_css_selector("[dataisright ='true']").click()
        time.sleep(1)
    print(d)
# 那路逗    ol56vw0RHmt_ryOuwWZtmlHaGQwg
# Polaris   ol56vwxTMwisjDZ80hx8HGqOtq1w
# OPPOfindX😊   ol56vwyhceW-n7nlV63JktG0-dX4
shanchu('ol56vwyhceW-n7nlV63JktG0-dX4')