#!/usr/bin/python
# coding=utf-8
# 李路
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pyperclip,pyautogui,os
# driver=webdriver.Chrome()
#  http://abbottcrm.chinanorth2.cloudapp.chinacloudapi.cn    abbottdev\Azureadmin   密码：Crmadmin123$%^
#{'domain': 'abbottcrm.chinanorth2.cloudapp.chinacloudapi.cn', 'path': '/', 'httpOnly': True, 'secure': False, 'expiry': 3129847365.046141, 'name': 'ReqClientId', 'value': 'afb5c04b-36a1-44b6-92d7-57e4563671ed'}
# coo={'domain': 'abbottcrm.chinanorth2.cloudapp.chinacloudapi.cn', 'path': '/', 'httpOnly': False, 'secure': False, 'value': 'HideNavTour', 'name': 'sessionNavTourCookie'}
# driver.get('http://abbottcrm.chinanorth2.cloudapp.chinacloudapi.cn')
#  cmd          chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\test"
# os.system(r"chrome.exe --remote-debugging-port=9222 --user-data-dir=D:\test1")
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
print(driver.title)
sleep(2)
driver.find_element_by_class_name('navTabButtonArrowDown').click()
sleep(2)
c=driver.find_element_by_xpath("//span[contains(@text, '会员管理')]")
sleep(2)
# c=driver.find_element_by_id('tempId_636810765156182908')
print(c)