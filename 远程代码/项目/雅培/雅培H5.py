#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路  %s,表示格化式一个对象为字符
# %d,整数

import pymssql, yaml, pandas, time
from selenium import webdriver

r = webdriver.Firefox()
r.get('https://abbotth5.wedochina.cn/question?useropenid=ow_TXjldoS4a29BbrLbIcnkbrH7M')

time.sleep(2)
d = r.find_element_by_css_selector("[class ='que-list auto ta-c']")
for i in  range(1,13):
    print(i)
    weizhi="li:nth-child(%s)"%(i)
    time.sleep(2)
    dd=d.find_element_by_css_selector(weizhi)
    time.sleep(2)
    dd.find_element_by_css_selector("[dataisright ='true']").click()
print(d)
r, quit()
