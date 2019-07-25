
#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
#pandas中有两类非常重要的数据结构，即序列Series和数据框DataFrame
import pandas, numpy
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
def demo3():
    file = pandas.ExcelWriter(r'd:\a.xls')
    f1 = pandas.DataFrame(numpy.random.randn(365, 4))
    f2 = pandas.DataFrame(numpy.random.randn(365, 4))
    # for i in range(1,4):
    f1.to_excel(excel_writer=file, sheet_name=str(1), encoding='utf-8')
    f2.to_excel(excel_writer=file, sheet_name=str(2), encoding='utf-8')
    file.save()
    file.close()
    print('ok')
import matplotlib.pyplot as plt
def demo4():
    df = pandas.DataFrame(numpy.random.randn(10,4),index=pandas.date_range('2018/12/18',
       periods=10), columns=['a','b','c','d'])
    df1 = pandas.DataFrame(numpy.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
    df1.plot.area()

    #条形图
    #柱状图
    #堆积图
    # bar或barh为条形
    # hist为直方图
    # box为盒型图
    # area为“面积”
    # scatter为散点图
    #pie饼状图
    plt.savefig(r'd:\a.jpg')
    plt.show()
def demo5():
    t=pandas.read_csv(r'd:\ee.csv')
    print(t.head())
demo4()