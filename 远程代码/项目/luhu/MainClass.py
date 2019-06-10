#!/usr/bin/python
# coding=utf-8
# ll 微信
from AppiumScript import OtherMethod
import time, datetime

nowtime = time.strftime("%Y-%m-%d %H:%M:%S")
print('开始：', nowtime)
a = datetime.datetime.now()

driver = OtherMethod.getdriver().driver1()
driver.find_element_by_accessibility_id("搜索").click()
time.sleep(1)
driver.find_element_by_id("com.tencent.mm:id/ji").send_keys('测试2号')
time.sleep(1)
driver.find_element_by_id("com.tencent.mm:id/om").click()
time.sleep(1)
driver.find_element_by_id("com.tencent.mm:id/mq").click()
# 用例  1
time.sleep(3)
contexts = driver.contexts
print(contexts)
# WebDriverWait.until()

size1 = driver.get_window_size()
width = size1['width']
print(width)
height = size1['height']
print(height)
for i in range(4):
    driver.swipe(width/2, height*3/4, width/2, height*1/4,200)
    time.sleep(1)

driver._switch_to.context('WEBVIEW_com.tencent.mm:tools')
print(driver.contexts)
driver.find_element_by_id("btn").click()
time.sleep(10)
driver.close_app()
driver.quit()
print('退出OK')
endtime = time.strftime("%Y-%m-%d %H:%M:%S")
print('结束', endtime)
b = datetime.datetime.now()
print('执行用例耗时', (b - a).seconds, '秒')
