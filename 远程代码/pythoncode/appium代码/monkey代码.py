#!/usr/bin/python
# -*- coding:utf8 -*-
#ll 微信 monkeyrunner
import time
def getDevice(mr):
    try:
        device = mr.waitForConnection()
        time.sleep(1)
        device.drag((540, 1920), (540, 960), 0.5, 1)
        print('open ok')
    except:
        print('抛出异常')
def openApp(device):
    package = 'com.tencent.mm'
    activity = 'com.tencent.mm.plugin.account.ui.ContactsSyncUI'
    runComponent = package + '/' + activity
    device.startActivity(component=runComponent)
    print('打开APP')
def uninstallApp(device):
    # 卸载方法 参数为 包名
    device.removePackage('com.tal.kaoyan')
    print('卸载')
def installApp(device):
    # apk的地址
    device.installPackage(r'E:\BaiduNetdiskDownload\kaoyan.apk')
    # apk的包名
    package = 'com.tal.kaoyan'
    # apk的activity
    activity = 'com.tal.kaoyan.ui.activity.splashActivity'
    runComponent = package + '/' + activity
    # 安装
    device.startActivity(component=runComponent)
    print('succss app....')
def dragApp(device):
    #点击
    device.touch(232, 699, 'DOWN_AND_UP')
    mr.sleep(2)
    print('chang an')
    # 拖动方法 参数为 起始位置  终止位置   总需时间  采取步骤
    device.drag((356, 976), (690, 976), 0.5, 1)
    mr.sleep(2)
    print('拖动OK')
def loginApp(device):
    # input输入值方法
    device.touch(115, 358, 'DOWN_AND_UP')
    mr.sleep(3)
    device.type('lilu2899')
    print('shuru mima')

    device.touch(300, 488, 'DOWN_AND_UP')
    mr.sleep(3)
    print('OK')

    # 截取当前屏幕方法，参数为指定位置 格式
    screenshot = device.takeSnapshot()
    screenshot.writeToFile(r'E:\app.png', 'png')
    print('jietu baocun')
def screenshotApp(device):
    # 获取截图，暂未成功
    result1 = device.takeSnapshot()
    # 将结果输出到文件,前面为路径，后面为图片类型，可写可不写
    result1.writeToFile('D:/demo1.png', 'png')
    # re=mr.loadImageFromFile('E:\app.png','png')
    # 将当前图像转换为一个特定的格式并将其作为字符串返回,然后你可以访问的iterable二进制字节。
    # result1.convertToBytes()
    # 图片的对比，先获取第二张截图
    result2 = device.takeSnapshot()
    result2.writeToFile('E:\demo1.png', 'png')
    # 判断图片相识度是否是为90%
    if (result1.sameAs(result2, 0.9)):
        print('ok')
    else:
        print('bu yi yang')