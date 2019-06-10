#!/usr/bin/python
# -*- coding:utf8 -*-
# ll 微信

import time


class kaiqi:
    def kaiqi1(driver):

        time.sleep(1)
        driver.find_element_by_id("开启探索 Link").click()
        a=driver.find_element_by_android_uiautomator("new UiSelector().description('开启探索')")
        print(a,'开启')
        # 跳转注册页面  用例 8
        time.sleep(5)
        try:
            driver.find_element_by_id("下滑发现更多")
            print('跳转开启正常5s')
        except:
            time.sleep(5)
            print('bug 跳转开启超时5s')
            # 上划
        driver.swipe(360, 1000, 0, 400, 200)
        time.sleep(1)
        # 输入内容
        driver.find_element_by_id("下滑发现更多").click()
        # 跳转注册页面  用例 8
