#!/usr/bin/python
# -*- coding:utf8 -*-
# ll adb devices
# wifi adb connect 192.168.12.50:5555
# 模拟器 adb connect 127.0.0.1:62001
# 线连 621QECPP2AGYZ
# 工具 uiautomatorviewer appium jmeter
# huawei UYT5T18518003924  cba00ff8   adb -s cba00ff8   tcpip 5559

from appium.webdriver.common.touch_action import TouchAction
import time,yaml,logging
from  appium import webdriver
class method:
    def getdrivce(self):
        capability={}
        f = open('Caps.yaml')
        d = yaml.load(f)
        capability['platformName']=d['platformName']
        capability['platformVersion']=d['platformVersion']
        capability['deviceName']=d['deviceName1']
        capability['appPackage']=d['appPackage']
        capability['appActivity']=d['appActivity']
        capability['noReset']=d['noReset']
        capability['unicodeKeyboard']=d['unicodeKeyboard']

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capability)
        driver.wait_activity(".ui.LauncherUI", 20, 1)
        return driver
    def open(self,driver):
        driver.find_element_by_accessibility_id("搜索").click()
        time.sleep(1)
        driver.find_element_by_id("com.tencent.mm:id/ji").send_keys('傲文管理')
        time.sleep(1)
        driver.find_element_by_id("com.tencent.mm:id/om").click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'瞬感自由会')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'会员中心new')]").click()
        # 用例  1
        time.sleep(10)
        contexts = driver.contexts
        print(contexts)
        # WebDriverWait.until()
        size1 = driver.get_window_size()
        width = size1['width']
        print(width)
        height = size1['height']
        print(height)
        for i in range(3):
            driver.swipe(width / 2, height * 3 / 4, width / 2, height * 1 / 4, 200)
            time.sleep(1)
            print('滑动', i+1)

    def slide(self,driver):
        #上划，必须放在原生context类型里，也就是nativeAPP
        size1 = driver.get_window_size()
        width = size1['width']
        print('width:',width)
        height = size1['height']
        print('height:',height)
        for i in range(2):
            #向上划
            driver.swipe(width / 2, height * 3 / 4, width / 2, height * 1 / 4, 200)
            print('上划', i + 1, '次')
            time.sleep(1)

    def getelement(self,driver):
        driver.find_element_by_accessibility_id("搜索").click()
        driver.find_element_by_id("com.tencent.mm:id/ji").send_keys('测试2号')
        driver.find_element_by_class_name("android.view.View")[1]
        driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'隐私政策')]").click()
        driver.find_element_by_xpath("//android.view.View[contains(@text,'隐私政策')]").click()
    def tuodong(self,driver):
        TouchAction(driver).long_press()
    def close(self,driver):
        #关闭
        driver.quit()
        #home 再次点开
        driver.close_app()
        driver.launch_app()
    def getcontext(self,driver):
        contexts = driver.contexts
        print(contexts)
        driver._switch_to.context('WEBVIEW_com.tencent.mm:tools')
    def getlog(self):
        logging.basicConfig(level=logging.INFO,filename='../YAMLXML/log.log',
                            format='时间:'+'%(asctime)s '+'位置：'+'%(filename)s [line:%(lineno)d] '+'内容：'+'%(levelname)s %(message)s')
        logging.info('ok')
        logging.error('error')
    def clearcache (self,driver):
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'我')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'设置')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'通用')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'微信存储空间')]").click()
        time.sleep(5)
        for i in range(3):
            driver.find_element_by_id("com.tencent.mm:id/jc").click()
            time.sleep(1)
            print(i + 1, 'ci')
        driver.find_element_by_id("com.tencent.mm:id/cw2").click()
        time.sleep(1)
        print('清理缓存OK')