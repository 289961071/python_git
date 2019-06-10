# coding=utf-8
# 李路
from selenium import webdriver
from time import sleep
import json,time
def gettoken():
    driver = webdriver.Firefox()
    # 无界面操作
    # driver = webdriver.PhantomJS()
    # driver.set_window_size(1366, 768)
    driver.get('https://wechat.katespade.aowenmarketing.com/login/login')
    driver.find_element_by_id('userName').send_keys('江成')
    driver.find_element_by_id('passWord').send_keys('Wedo8888')
    cook=[{'domain': 'wechat.katespade.aowenmarketing.com', 'secure': False, 'name': 'ASP.NET_SessionId', 'httpOnly': True, 'path': '/', 'value': 'o5tghfd3d0sbmw1jrg2m3ehq'}]
    sleep(10)
    a = driver.get_cookies()
    f1=open(r'E:\LL\cook.txt','w')
    f1.write(json.dumps(a))
    f1.close()
    print(a)
def settoken():
    f1=open(r'E:\LL\cook.txt')
    cook=json.loads(f1.read())
    driver = webdriver.Firefox()
    driver.get('https://wechat.katespade.aowenmarketing.com/login/login')
    time.sleep(5)
    for i in  cook:
        driver.add_cookie(i)
    print('ok')
    print(driver.get_cookies())
    driver.refresh()
settoken()