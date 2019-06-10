#!/usr/bin/python
# -*- coding:utf8 -*-
# ll 微信
import time


class tiyan:
    def tiyan1(driver):
        # 上划正常 用例 2
        driver.swipe(360, 1000, 0, 400, 200)
        time.sleep(1)
        # 已付款确认参与用户
        driver.find_element_by_id("我是体验官 Link").click()
        # d等待跳转5s  用例3
        time.sleep(5)
        try:
            driver.find_element_by_id("藏地体验官-发现日记 Link")
            print('跳转藏地体验官正常5s')
        except:
            time.sleep(5)
            print('bug 跳转藏地体验官超时5s')

            # 上划  用例 3
        driver.swipe(360, 1000, 0, 400, 200)
        time.sleep(1)
        driver.find_element_by_id("藏地体验官-发现日记 Link").click()
        # 跳转注册页面  用例 8
        time.sleep(5)
        try:
            driver.find_element_by_id("发送验证码")
            print('跳转注册正常5s')
        except:
            time.sleep(5)
            print('bug 跳转注册超时5s')
            # 上划
        driver.swipe(360, 1000, 0, 400, 200)

