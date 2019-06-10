# coding=utf-8
# 李路  200811028<love051119@163.com> shiyierzhon@qq.com
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.execute_script('window.open()')
print(driver.window_handles)
# time.sleep(10)
# driver.switch_to.window(driver.window_handles[1])
# driver.get('https://www.taobao.com')
# time.sleep(1)
# driver.switch_to.window(driver.window_handles[0])
# driver.get('http://www.w3school.com.cn/tags/tag_img.asp')
driver.switch_to.alert()