#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
import time,sys
def pro(num,to):
    rt=float(num)/to
    rn=int(100*rt)
    r='\r[{}{}]{}%'.format('*'*rn,' '*(100-rn),rn)
    sys.stdout.write(r)
    sys.stdout.flush()
i,n=0,100
for i in range(n):
    time.sleep(0.1)
    pro(i+1,n)
