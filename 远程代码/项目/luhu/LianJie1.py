#!/usr/bin/python
# -*- coding:utf8 -*-
# ll 微信
from appiumJ import login2
import urllib3
import time, datetime


class login:
    def login1(driver):
        # 先等待3s，再点击公众号
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'通讯录')]").click()
        time.sleep(1)
        driver.find_element_by_id("搜索").click()
        time.sleep(1)
        # driver.find_element_by_id("com.tencent.mm:id/ji").send_keys('2 hao')
        driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'搜索')]").send_keys("3")
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'测试3号')]").click()
        time.sleep(2)
        # xpath正确用法，累
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'测试3号')]").click()
        # 用例  1
        time.sleep(5)
        try:
            if driver.find_element_by_accessibility_id("我是体验官 Link"):
                print('未注册链接正常5s')

            if driver.find_element_by_accessibility_id("我的日记"):
                print('未注册链接正常5s')
        except:
            time.sleep(10)
            print('bug 链接超时5s')  # 直接点击， 上面的链接超过5s，视为严重bug





