#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
#pandas中有两类非常重要的数据结构，即序列Series和数据框DataFrame
import pandas,numpy
def demo1():
    ar=numpy.arange(10)
    print(type(ar))
    arr=pandas.Series(ar)
    print(type(arr))
def demo2():
    dic1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
    arr = pandas.Series(dic1)
    print(type(arr))
    print(arr)
demo2()