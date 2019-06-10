#!/usr/bin/python
# -*- coding:utf8 -*-
# ll 微信
import time


class quanxin:
    def quanxin1(driver):

        time.sleep(1)
        driver.find_element_by_id("全新探索 Link").click()
        # 跳转注册页面  用例 8
        time.sleep(5)
        try:
            driver.find_element_by_id("发现大礼 Link")
            print('跳转发现正常5s')
        except:
            time.sleep(5)
            print('bug 跳转发现超时5s')
            # 上划
        driver.swipe(360, 1000, 0, 400, 200)
        time.sleep(1)
        # 输入内容
        driver.find_element_by_id("发现大礼 Link").click()
        # 跳转注册页面  用例 8








