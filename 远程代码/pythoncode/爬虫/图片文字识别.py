#!/usr/bin/python
# coding=utf-8
# 李路
from PIL import Image
import pytesseract, pandas

# 上面都是导包，只需要下面这一行就能实现图片文字识别  解毒代码  TASKKILL /F /IM cmd.exe /T
# text = pytesseract.image_to_string(Image.open(r"E:\LL\a.png"), lang='chi_sim').strip()
text = pytesseract.image_to_string(Image.open(r"a.png")).strip()
print(text)
with open('d:/ee.csv', mode='wb') as f:
    f.write(text.encode())
    print('ok')
