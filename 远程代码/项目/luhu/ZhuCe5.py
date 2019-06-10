#!/usr/bin/python
# -*- coding:utf8 -*-
# ll 微信
import time
class zhuce:
    def zhuce1(driver):
        driver.swipe(360, 1000, 0, 400, 200)
        time.sleep(2)
        # 直接提交，弹框提交，重置
        driver.find_element_by_xpath("//android.view.View[contains(@text，'提交')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//android.view.View[contains(@text，'确定')]").click()
        time.sleep(1)
        #验证姓名，没有限制就空格限制空
        driver.find_element_by_xpath("//android.widget.EditText[contains(@text，'姓名')]").send_keys(' ')
        driver.find_element_by_xpath("//android.widget.EditText[contains(@text，'女士')]").send_keys(' ')
        driver.find_element_by_xpath("//android.widget.EditText[contains(@text，'先生')]").send_keys(' ')
        driver.find_element_by_accessibility_id("iphone")
        driver.find_element_by_accessibility_id("code")
        driver.find_element_by_accessibility_id("code")
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.Button[contains(@text，'发送验证码')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//android.view.View[contains(@text，'省')]").click()
        driver.find_element_by_xpath("//android.view.View[contains(@text，'市')]").click()
        driver.find_element_by_xpath("//android.view.View[contains(@text，'选择经销商?')]").click()
        driver.find_element_by_xpath("//android.view.View[contains(@text，'您感兴趣的路虎车型?')]").click()
        driver.find_element_by_xpath("//android.view.View[contains(@text，'我已阅读并接受')]").click()
        driver.find_element_by_xpath("//android.view.View[contains(@content-desc，'隐私政策')]").click()
        time.sleep(1)
        # 输入内容  姓名
        driver.find_element_by_xpath("//android.view.View[contains(@index,3)]").send_keys(u'中文ok')
        time.sleep(1)
        # 输入内容  手机
        driver.find_element_by_xpath("//android.view.View[contains(@text，'确定')]").click()
        driver.find_element_by_xpath("//android.view.View[contains(@text，'提交')]").click()
        driver.find_element_by_xpath("//android.view.View[contains(@text，'重置')]").click()

        # 输入内容

        driver.find_element_by_xpath("//android.view.View[contains(@index,6)]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.TextViewcontains(@text,'1212')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.Button[contains(@index,13)]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.TextViewcontains(@text,'1212')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//android.view.View[contains(@text，'note-1')]")
