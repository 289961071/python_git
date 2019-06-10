#!/usr/bin/python
# -*- coding:utf8 -*-

from time import sleep, ctime

import yaml,logging,os
logging.basicConfig(level=logging.INFO,filename='..\YAMLXML\demo1.log',
                    format='时间:'+'%(asctime)s '+'位置：'+'%(filename)s [line:%(lineno)d] '+'内容：'+'%(levelname)s %(message)s')
r=os.system(r"adb connect 192.168.12.50:5555")
logging.info('\033[1;31m\033[0m')
sleep(1)
logging.error('错误')
sleep(2)
logging.debug('错误调试')
logging.warning('错误警告')
print('\033[1;31m链接到WiFi\033[0m')

