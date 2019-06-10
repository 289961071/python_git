#!/usr/bin/python
# -*- coding:utf8 -*-
#ll 微信 monkeyrunner
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
import time

print(time.strftime("%H:%M:%S"))
device = mr.waitForConnection()
package = 'com.tencent.mm'
activity = 'com.tencent.mm.plugin.account.ui.ContactsSyncUI'
runComponent = package + '/' + activity
device.startActivity(component=runComponent)
print('yi lian jie')