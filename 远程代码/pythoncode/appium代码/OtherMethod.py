#!/usr/bin/python
# -*- coding:utf8 -*-
import os


def DevicesList():
    p = os.popen('adb devices')
    dList = p.read()
    p.close()
    lists = dList.split("\n")
    dName = []
    for i in lists:
        if (i.strip() == ""):
            continue
        elif (i.startswith("List of")):
            continue
        else:
            dName.append(i.split("\t")[0])
    return dName
