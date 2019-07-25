#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路  其实没看懂。。。

import numpy as np
import random

arr = np.arange(1, 11)
print(arr)  # 生成1-10的一维数组
for i in range(10):  # i = [0,9]
    # print(i)
    tmp = random.randint(i, 9)  # 生成一个[i,9]的随机数
    arr[i], arr[tmp] = arr[tmp], arr[i]  # 注意这里是对数组内部的元素进行交换

print(arr)