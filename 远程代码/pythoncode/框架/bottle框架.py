#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
from bottle import request, run, route, static_file,response,template,Bottle
from 框架 import datebase
# app=Bottle()
@route('/:path#.+#')
def login_from(path):
    return static_file(path, root='/static')

@route('/aaa', method='post')
def yanzheng():
    #response.content_type = 'text/html; charset=latin9'
    #post方法request.forms.get('name') get方法request.GET.get('name')
    name = request.forms.get('name')
    pwd = request.forms.get('pwd')
    a = datebase.shujuku(name, pwd)
    if a == 'ok':
        print(a, '数据库调用成功')
        return '数据库调用成功'
    else:
        print(a,'数据库调用失败')
        return static_file('bbb.html',root='E:\LL\Allcode\Python\框架\templates')
        # return response.set_header('cook1','bubububu')

run(host='localhost', port=8080, debug=True)
