#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路

import pymssql, yaml, pandas, time, requests
from selenium import webdriver


#  tPnkk6WSeOYM+
#  wedo9k*$61ACGh%3   正式

def liulan():
    r = webdriver.Firefox()
    r.get('https://wechat.abbottdiabetes.syswechat.com/SystemManage/QRCode')
    return r


def demo():
    r = liulan()
    time.sleep(20)
    zhi = {}
    try:
        for i in range(1, 400):
            zhi1 = {}
            k = r.find_element_by_id("qrsceneId").get_attribute('value')
            if int(k) > 400:
                print('到达400')
                time.sleep(30)
            time.sleep(2)
            r.find_element_by_id("actionName").send_keys(k)
            time.sleep(2)
            r.find_element_by_xpath("//input[contains(@class, 'c-btn btn-blue')]").click()
            time.sleep(2)
            r.find_element_by_xpath("//button[contains(@class, 'aui_state_highlight')]").click()
            time.sleep(2)
            v = r.find_element_by_id("qrUrl").get_attribute('value')
            zhi[k] = v
            zhi1[k] = v
            df = pandas.DataFrame(pandas.Series(zhi1))
            df.to_csv(r'd:\雅培正式二维码.csv', mode='a', encoding='utf-8')
            print(k, v)
    except IOError:
        print('处理失败')
        print(zhi)
        df = pandas.DataFrame(pandas.Series(zhi))
        df.to_csv(r'd:\雅培二维码总.csv', mode='a', encoding='utf-8')


def pachong(WXSourceid, ticket):
    # r = requests.get('https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket= %s'%(ticket))
    ur=r'https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s'%(ticket)
    r = requests.get(ur)
    image = r.content
    jpg = r"D:\正式二维码\正式%s.jpg" % (WXSourceid)
    print("保存图片" + jpg + "\n")
    fb = open(jpg, "wb")
    fb.write(image)
    print(WXSourceid, 'ok')


def shujuku():
    d = yaml.load(open(r'D:\Caps.yaml'))
    con = pymssql.connect(host=d['yp_server'], port=d['yp_port'], user=d['yp_user'], password=str(d['yp_pwd']),
                          database=d['yp_db'])
    cuesor = con.cursor()
    sql = "select  WXSourceid,ticket from WXQRCodeLimit where WXSourceid <401 and WXSourceid >0  ORDER BY id desc"
    cuesor.execute(sql)
    row = cuesor.fetchall()
    return row


# pachong('422.jpg')得
s = shujuku()
for i in s:
    pachong(i[0], i[1])
