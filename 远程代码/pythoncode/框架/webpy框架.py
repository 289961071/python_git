#!/usr/bin/python
# coding=utf-8
# 李路
import web

urls = (
    '/aaa', 'aaa',
    '/upload', 'upload',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())
#模板公共变量

render = web.template.render('templates/')


class aaa:
    def GET(self):
        return render.blog()
        # return open('E:\LL\Allcode\Python代码\框架\templates\blog.html',encoding='gbk')
        #  raise web.seeother('')
class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'
class upload:
    def POST(self, name):
        #获取请求 无论get post
        q=web.input()
        #获取请求头
        qheard=web.ctx
        print(q)
        return render.bbb(q)

if __name__ == "__main__":
    app.run()
