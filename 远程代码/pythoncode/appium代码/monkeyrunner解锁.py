#!/usr/bin/python
# -*- coding:utf8 -*-
#ll 微信 monkeyrunner
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
import time
try:
    device = mr.waitForConnection()
    time.sleep(1)
    device.drag((540, 900), (540, 100), 0.1)
    print('上划解锁ok')
except:
    print('抛出异常')
