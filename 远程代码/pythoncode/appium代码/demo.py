#!/usr/bin/python
# -*- coding:utf8 -*-
import time, os, logging

logging.basicConfig(level=logging.INFO, filename='log.log',
                    format='时间:' + '%(asctime)s ' + '位置：' + '%(filename)s [line:%(lineno)d] ' + '内容：' + '%(levelname)s %(message)s')


def dayin():
    r = os.popen(r"adb connect 192.168.12.50:5555").read()
    if 'already' in r:
        m = os.popen(r"adb devices").read()
        logging.info('已经链接到WiFi')
        print('\033[1;31m', m, '\033[0m')
    else:
        time.sleep(5)
        os.system(r"adb devices")
        logging.info('刚链接到WiFi')
        print('\033[1;31m', r, '\033[0m')

dayin()