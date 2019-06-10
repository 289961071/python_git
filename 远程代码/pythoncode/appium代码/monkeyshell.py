#!/usr/bin/python
# -*- coding:utf8 -*-
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
# 不能调用方法
from time import sleep, ctime
import time,threading
name1="192.168.12.50:5555"
name2="192.168.12.128:5559"
def dxc(name):
    device1 = mr.waitForConnection(name)
    device1.drag((540, 900), (540, 100), 0.1)
    print(name,'open')
list = [name1, name2]
threads = []
files = range(len(list))
for i in files:
    t = threading.Thread(target=dxc, args=(list[i],))
    threads.append(t)
if True:
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

