
#!/usr/bin/python
# -*- coding:utf8 -*-
# 李路
import pandas, numpy

file = pandas.ExcelWriter(r'd:\a.xls')
f1 = pandas.DataFrame(numpy.random.randn(365, 4))
f2 = pandas.DataFrame(numpy.random.randn(365, 4))
# for i in range(1,4):
f1.to_excel(excel_writer=file, sheet_name=str(1), encoding='utf-8')
f2.to_excel(excel_writer=file, sheet_name=str(2), encoding='utf-8')
file.save()
file.close()
print('ok')