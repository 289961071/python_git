#!/usr/bin/python
# coding=utf-8
# 李路
from geopy.geocoders import Nominatim
import json

#根据名字查详细地址和坐标
def jw1():
    g = Nominatim()
    loc = g.geocode('上海大学')
    print(loc.address)
    print(loc.latitude, loc.longitude)
def jw2():
    g = Nominatim()
    loc = g.reverse("")
    print(loc.address)
g = Nominatim()
loc = g.geocode('上海大学')
print(loc.address)
print(loc.latitude, loc.longitude)