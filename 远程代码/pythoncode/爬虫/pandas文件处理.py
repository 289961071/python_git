
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
    # print(df[1:6])
    # print('index:',df[1:6].index)
    # print('columns:',df[1:6].columns)
    # print('values:',df[1:6].values)
    # a=df[1:6].values
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
def cs1():
    # 导入CSV xlsx
    df = pandas.DataFrame(pandas.read_excel(r'd:\a.xls'))
    df = pandas.DataFrame(pandas.read_csv(r'd:\ee.csv'))
    print(df)


def cs2():
    # DataFrame 格式化数据  第一个是文件  第二个是列名
    f = pandas.read_excel(r'd:\a.xls')
    df = pandas.DataFrame(f, columns=['a', 'b''c', 'd'])
    print(df)


def cs3():
    # DataFrame 格式化数据  第一个是文件  第二个是列名
    f = pandas.read_excel(r'd:\a.xls')
    df = pandas.DataFrame(f)
    # print(df.info())  数据表基本信息（维度、列名称、数据格式、所占空间等）
    # print(df.dtypes) 每一列数据的格式  df[‘B’].dtype 指定列数据格式
    print(df.isnull())  # 空值
    print(df.isna())  # 缺失值
    # print(df['Id'].unique()) 查看某一列的唯一值
    # df.values 查看数据表的值： df.columns 查看列名称
    # print(df.head()) 默认前5 行数据  可以指定行数
    # print(df.tail(4))  默认后5 行数据  可以指定行数


# 数据表清洗
def cs4():
    # DataFrame 格式化数据  第一个是文件  第二个是列名
    f = pandas.read_excel(r'd:\a.xls')
    df = pandas.DataFrame(f)
    # 1、用数字0填充缺失值：空值：在pandas中的空值是""
    # 缺失值：在dataframe中为nan或者naT（缺失时间），在series中为none或者nan即可
    # print(df.fillna(2,inplace=True))
    # 2、使用列prince的均值对NA进行填充：
    # df[‘prince’].fillna(df[‘prince’].mean())
    # 3、清楚city字段的字符空格：
    # df[‘city’]=df[‘city’].map(str.strip)
    # 4、大小写转换：
    # df[‘city’]=df[‘city’].str.lower()
    # 5、更改数据格式：
    # df[‘price’].astype(‘int’)
    # 6、更改列名称：
    # df.rename(columns={‘category’: ‘category - size’})
    # 7、删除后出现的重复值：
    # df[‘city’].drop_duplicates()
    # 8、删除先出现的重复值：
    # df[‘city’].drop_duplicates(keep=’last’)
    # 9、数据替换：
    # print(df.replace('0', '2'))
    # 10、删除 行 列
    # print(df.drop(columns=['o'], inplace=True))
    print(df.drop([10,20],inplace=True))
    df.to_excel(r'd:\a.xls')

def cs5():
    f = pandas.read_excel(r'd:\a.xls',sheet_name=1,)
    print(f)
    df = pandas.DataFrame(f,columns=['a','b'])
    df1 = pandas.DataFrame(numpy.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
    df['a'].plot.pie(subplots=True)
    plt.savefig(r'd:\a.jpg')
    plt.show()
cs5()

