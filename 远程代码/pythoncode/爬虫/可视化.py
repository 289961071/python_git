# coding=utf-8
# 李路
import numpy as np
import numpy.random as rnd
from matplotlib import pyplot as plt
from pylab import *
# 解决中文显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei']
def zhixian():
    x = np.arange(4, 11)
    y = 2 * x + 5
    plt.title("Matplotlib demo")
    plt.xlabel("x zhou")
    plt.ylabel("y zhou")
    plt.plot(x, y)
    plt.show()

def dian():
    x = np.arange(1, 11)
    y = 2 * x + 5
    plt.title("Matplotlib demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    plt.plot(x, y, "ob")
    plt.show()

def xuan():
    # 计算正弦曲线上点的 x 和 y 坐标
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)
    plt.title("sine wave form")
    # 使用 matplotlib 来绘制点
    plt.plot(x, y)
    plt.show()

def fangkuai():
    x = [5, 8, 10]
    y = [12, 16, 6]
    x2 = [6, 9, 11]
    y2 = [6, 15, 7]
    plt.bar(x, y, align='center')
    plt.bar(x2, y2, color='g', align='center')
    plt.title('Bar graph')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()
def tu():
    # 定义图像数据
    a = np.linspace(0, 1, 9).reshape(3, 3)
    # 显示图像数据
    plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
    # 添加颜色条
    plt.colorbar()
    # 去掉坐标轴
    plt.xticks(())
    plt.yticks(())
    plt.show()
def sekuai():
    labels = '游戏', '音乐', '拍照', '其他'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
sekuai()