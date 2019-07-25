# coding=utf-8
# ll 微信 monkeyrunner
# /***
#  *_______________#########_______________________
#  *______________############_____________________
#  *______________#############____________________
#  *_____________##__###########___________________
#  *____________###__######_#####__________________
#  *____________###_#######___####_________________
#  *___________###__##########_####________________
#  *__________####__###########_####_______________
#  *________#####___###########__#####_____________
#  *_______######___###_########___#####___________
#  *_______#####___###___########___######_________
#  *______######___###__###########___######_______
#  *_____######___####_##############__######______
#  *____#######__#####################_#######_____
#  *____#######__##############################____
#  *___#######__######_#################_#######___
#  *___#######__######_######_#########___######___
#  *___#######____##__######___######_____######___
#  *___#######________######____#####_____#####____
#  *____######________#####_____#####_____####_____
#  *_____#####________####______#####_____###______
#  *______#####______;###________###______#________
#  *________##_______####________####______________
<<<<<<< HEAD
#  */
# import pandas, numpy

id = [
    'ogb9a1GH3P0MiWSyMWoF_BAec_3o',
    'ogb9a1H9JJAK95K3QHUKfjB3yaaQ',
    'ogb9a1FselRKRTlCdCe0N3qoRMXM',
    'ogb9a1MI-4FrAFgqhB_F74oje5zw',
    'ogb9a1KILmE2xMCPvJsXuAPERXug',
    'ogb9a1NalGz_F3PL1sRYeKr8JaiE',
    'ogb9a1FomDNQoks5HpRWlOft2TCs',
    'ogb9a1HMTnqwSQ_y0lCvLbgsyP5E',
]
=======
#  *

<<<<<<< HEAD
def cs1():
    # 导入CSV xlsx
    df = pandas.DataFrame(pandas.read_excel(r'd:\a.xls'))
    df = pandas.DataFrame(pandas.read_csv(r'd:\ee.csv'))
    print(df)

>>>>>>> 1a15c0d90758bb36e24eebaf4e6eca5c3964f2c7

def cs2():
    # DataFrame 格式化数据  第一个是文件  第二个是列名
    f = pandas.read_excel(r'd:\a.xls')
    df = pandas.DataFrame(f, columns=['a', 'b''c', 'd'])
    print(df)

<<<<<<< HEAD
def cs(shouji):
    s = "select * from Run_UserFriend  WHERE Inviter=%s " % shouji
    print(s)
=======
>>>>>>> 1a15c0d90758bb36e24eebaf4e6eca5c3964f2c7

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

<<<<<<< HEAD
cs('ok')
=======

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
>>>>>>> 1a15c0d90758bb36e24eebaf4e6eca5c3964f2c7
=======
a=[x for  x in range(6)]
print(a)
>>>>>>> dd40c942913e98c4a8647a8fdde5e836af70cef8
