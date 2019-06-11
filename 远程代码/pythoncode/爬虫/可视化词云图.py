# coding=utf-8
# 李路
import jieba
from matplotlib import pyplot as plt
from wordcloud import ImageColorGenerator,STOPWORDS,WordCloud
from scipy.misc import imread # 这是一个处理图像的函数

back_color=imread('timg.jpg') # 解析该图片

wc = WordCloud(background_color='white',  # 背景颜色
               scale=32,#scale属性，该值越大越清楚
               max_words=50,  # 最大词数
               mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
               max_font_size=120,  # 显示字体的最大值
               stopwords=STOPWORDS.add('习近平'),  # 使用内置的屏蔽词，再添加'苟利国'
               # font_path="C:/Windows/Fonts/STFANGSO.ttf",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体 也可以去
               # Wordcloud.py 28行 修改引用的字体包  前提是把字体包放入 这个模块
               random_state=42,  # 为每个词返回一个PIL颜色
               # width=1000,  # 图片的宽
               # height=860  #图片的长
               mode='RGBA'
               )
# 添加自己的词库分词，比如添加'金三胖'到jieba词库后，当你处理的文本中含有金三胖这个词，
# 就会直接将'金三胖'当作一个词，而不会得到'金三'或'三胖'这样的词
jieba.add_word('大师兄')

# 打开词源的文本文件
text = open(r'd:\b站弹幕.csv',encoding='gbk').read()

wc.generate(text)
# 基于彩色图像生成相应彩色
image_colors = ImageColorGenerator(back_color)
# 显示图片
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 绘制词云
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')
# 保存图片
wc.to_file('19th.png')