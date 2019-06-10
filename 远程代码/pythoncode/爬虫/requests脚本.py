#!/usr/bin/python
# -*- coding:utf8 -*-
import requests, json


def demo1():
    # 获取token  get方法参数为params  post方法参数为data
    value = {'appid': 'crm.wedo', 'APPsecret': 'crm.wedo'}
    r = requests.get('https://gwdev.rfc-china.com:8888/api/sso/access_token', params=value)
    # 不知道什么原因 返回的字典无法正常输入  需要转换为正常的json参数
    d = json.loads(r.text)['data']
    print(d)
    print(r.status_code)
    print(r.json())
    # 调用第二个接口  给出token
    head = {'Authorization': 'bearer ' + d}
    value2 = {'campaignId': '212', 'usercode': 'fmc01', 'shopcode': '00014169'}
    r2 = requests.get('https://gwdev.rfc-china.com:8888/api/idream/campaigngift/getstockinfo', headers=head,
                      params=value2)
    print(r2.json())


def demo2():
    # 请求
    r = requests.get('https://api.github.com/events')
    r = requests.post('http://httpbin.org/post', data={'key': 'value'}, )
    # 其他HTTP请求方式
    # HEAD请求获取URL位置资源的响应消息报告，即获得资源的头部信息
    # PUT请求向URL位置存储一个资源，覆盖原URL位置的资源
    # PATCH请求局部更新URL位置的资源,即改变该处资源的部分内容
    # DELETE请求删除URL位置存储的资源

    r = requests.put('http://httpbin.org/put', data={'key': 'value'})
    r = requests.delete('http://httpbin.org/delete')
    r = requests.head('http://httpbin.org/get')
    r = requests.options('http://httpbin.org/get')
    # 参数  get是params  post 是 data 注意字典里值为 None 的键都不会被添加到 URL 的查询字符串里。json参数格式化下
    # 由于发送json格式数据太常见了，所以在Requests模块的高版本中，又加入了json这个关键字参数，
    # 可以直接发送json数据给post请求而不用再使用json模块了
    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
    r = requests.get('http://httpbin.org/get', params=json.dumps(payload), json=payload)
    print(r.url)  # 编码后的URL
    # http: // httpbin.org / get?key1 = value1 & key2 = value2 & key2 = value3

    # 响应
    r.encoding()  # 输出编码格式
    r.text()  # 获取访问信息  响应的字符串形式
    r.encoding = 'ISO-8859-1'  # 修改编码 然后在输出
    # u'[{"repository":{"open_issues":0,"url":"https://github.com/..
    r.status_code()  # 响应状态码 200表示成功 可以用requests.codes.ok来指代200这个返回值：
    #理解Response编码
    #r.encoding:如果header中不存在charset,则认为编码是ISO-8859-1,r.text根据r.encoding显示网页内容
    #r.apparent_encoding:根据网页内容分析处的编码方式可以看做是r.encoding的备选

    #请求异常
    #requests.ConnectionError网络连接异常，如DNS查询失败，拒绝连接等
    # requests.HTTPErrorHTTP错误异常
    # requests.URLRequiredURL缺失异常
    # requests.TooManyRedirects超过最大重定向次数，产生重定向异常
    # requests.ConnectTimeout连接远程服务器超时异常
    # requests.Timeout请求URL超时，产生超时异常
    #参数
    #params: 字典或字节序列，作为参数增加到url中

    #data:字典，字节序列或文件对象,作为Request的内容
    #json: JSON格式的数据，作为Request的内容
    #headers: 字典, HTTP定制头
    #cookie: 字典或CooKiJar, Request中的cookie
    #auth: 元祖，支持HTTP认证功能
    #files: 字典类型，传输文件
    #timeout: 设定超时时间，秒为单位
    #proxies: 字典类型，设定访问代理服务器，可以增加登录认证
    #allow_redirects: True/False,默认为True,重定向开关
    #stream: True/False，默认为True,获取内容立即下载开关
    #verity: True/False默认Ture,认证ssl证书开关
    #cert: 本地ssl证书路径


def demo3():
    # 请求一个图片地址并且要保存图片的话
    def saveImage(imgUrl, imgName="default.jpg"):
        r = requests.get(imgUrl, stream=True)
        image = r.content
        jpg = "D:\a" + imgName
        print("保存图片" + jpg + "\n")
        try:
            with open(jpg, "wb") as jpg:
                jpg.write(image)
                return
        except IOError:
            print("IO Error")
            return
        finally:
            jpg.close()

def demo4():
    #r.headers｀返回的是一个字典
    a={
        'content-encoding': 'gzip',
        'transfer-encoding': 'chunked',
        'connection': 'close',
        'server': 'nginx/1.0.4',
        'x-runtime': '147ms',
        'etag': '"e1ca502697e5c9317743dc078f67693a"',
        'content-type': 'application/json'
    }
    headers = {'user-agent': 'myagent'}
    r = requests.get("http://pythontab.com/justTest", headers=headers)
    #获取cookie
    cookies=r.cookies(['example_cookie_name'])
    #发送cookie
    r = requests.get('url', cookies=cookies)
    r.history() #查看重定向
    #allow_redirects 参数 来禁止重定向
    r = requests.get('http://pythontab.com', allow_redirects=False)
    #timeout参数来设定url的请求超时时间
    requests.get('http://pythontab.com', timeout=1)
def demo5():
    #指定代理来进行http或https访问（使用proxies关键字参数）
    proxies = {
        "http": "http://10.10.1.10:3128",
        "https": "http://10.10.1.10:1080",
    }
    requests.get("http://pythontab.com", proxies=proxies)
    #session  使用网站的登录api进行登录，然后得到session，最后就可以用这个session来请求其他url了
    s = requests.Session()
    login_data = {'form_email': 'youremail@example.com', 'form_password': 'yourpassword'}
    s.post("http://pythontab.com/testLogin", login_data)
    r = s.get('http://pythontab.com/notification/')
    print (r.text)

    #下载页面
    r = requests.get("http://www.pythontab.com")
    with open("haha.html", "wb") as html:
        html.write(r.content)
    html.close()

def demo():
    r = requests.get('http://pythontab.com/',allow_redirects=False)
    a=r.url
    c=r.history
    print(a)


demo()















