#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
import pandas
zhi={'57': 'https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=gQFN8TwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyT01wRVpvM1FibmUxMDAwMDAwM2cAAgS1ykJdAwQAAAAA',
     '56': 'https://mp.weixin.qq.com/cgi-bin/sh'}
df = pandas.DataFrame(pandas.Series(zhi))
df.to_csv(r'd:\雅培二维码.csv', mode='a',encoding='utf-8')