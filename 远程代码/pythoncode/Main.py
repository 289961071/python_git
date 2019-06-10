#!/usr/bin/python
# coding=utf-8
# ll 微信
from AppiumScript import OtherMethod
from AppiumScript import Method
import threading
import time, datetime

nowtime = time.strftime("%Y-%m-%d %H:%M:%S")
print('开始：', nowtime)
a = datetime.datetime.now()

driver2 = OtherMethod.getdriver().driver2()
driver1 = OtherMethod.getdriver().driver1()


def thread1(self,driver):
    Method.method().open(driver2)
    driver.close_app()
    driver.launch_app()
    time.sleep(5)
    b = Method.method().clearcache(driver)
    time.sleep(1)
    driver.open_notifications()
    driver.quit()


threads = []
lists = [driver1, driver2]
for i in range(2):
    t = threading.Thread(target=thread1, args=lists[i])
    threads.append(t)
if __name__ == '__main__':
    for i in range(2):
        threads[i].start()
    for i in range(2):
        threads[i].join()

print('退出OK')
time.sleep(10)
endtime = time.strftime("%Y-%m-%d %H:%M:%S")
print('结束', endtime)
b = datetime.datetime.now()
print('执行用例耗时', (b - a).seconds, '秒')
