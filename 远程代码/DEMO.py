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
#  */

import jieba
from matplotlib import pyplot as plt
from wordcloud import ImageColorGenerator,STOPWORDS,WordCloud
from scipy.misc import imread # 这是一个处理图像的函数

#back_color=imread('a.jpg') # 解析该图片

wc = WordCloud(background_color='white',  # 背景颜色
                width=500,  # 图片的宽
                height=500  #图片的长
               )
#jieba.add_word('大师兄')

text = open(r'D:\b站弹幕2.csv','r',encoding='gbk').read()
wc.generate(text)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file('1th.png')