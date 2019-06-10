#!/usr/bin/python
# -*- coding:utf8 -*-
#ll 微信 monkeyrunner
import threading
def dxc(name):
    print('\033[0;31m' + name + '\033[0m')
lists = ['x', 'y']
threads = []
for i in range(len(lists)):
    t = threading.Thread(target=dxc, args=(lists[i],))
    threads.append(t)
if __name__ == '__main__':
    for i in threads:
        i.start()
    for i in threads:
        i.join()
