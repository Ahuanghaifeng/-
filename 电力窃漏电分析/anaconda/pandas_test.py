# coding=utf-8
# import pandas as pd
# # 读取csv文件 3列取名为 name,sex,births，后面参数格式为names=
# names1880 = pd.read_csv("names_1880.txt", names=['name', 'sex', 'births'])
# print names1880
# print names1880.groupby('sex').births.sum()

# def add_prop(group):
#     births = group.births.astype(float)
#     group['prop'] = births/births.sum()
#     return group
#
# names = names1880.groupby(['year', 'sex']).apply(add_prop)


import pandas as pd
import matplotlib as mb
import matplotlib.pyplot as plt
xls = pd.read_excel('phase_detector.xlsx',names=['x','y'])
print xls
# 原点相交
ax = plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
# 去掉边框
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
plt.plot(xls.x, xls.y)
plt.scatter(xls.x, xls.y)
plt.savefig('aa.png')
plt.show()
