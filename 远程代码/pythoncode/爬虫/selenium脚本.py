#!/usr/bin/python
# coding=utf-8
from selenium import webdriver
r=webdriver.Firefox()
#  http://abbottcrm.chinanorth2.cloudapp.chinacloudapi.cn    abbottdev\Azureadmin   密码：Crmadmin123$%^
r.get('http://abbottcrm.chinanorth2.cloudapp.chinacloudapi.cn')
# r.implicitly_wait(3)
a=r.switch_to.alert()
print(a)
a.text()
a.send_keys('abbottdev\Azureadmin')
a.dismiss()
a.accept()
r.get_screenshot_as_file('E:\a.png')
r.maximize_window()
r,quit()