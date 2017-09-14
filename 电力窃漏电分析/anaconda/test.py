#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 10, 1000)
# y = np.sin(x)
# z = np.cos(x**2)
#
# plt.figure(figsize=(8,4))
# plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
# plt.plot(x,z,"b--",label="$cos(x^2)$")
# plt.xlabel("Time(s)")
# plt.ylabel("Volt")
# plt.title("PyPlot First Example")
# plt.ylim(-1.2,1.2)
# plt.legend()
# plt.show()
# from numpy import *
# import matplotlib.pyplot as plt
#
# x = linspace(0, 5, 10)
# y = x ** 2
# fig = plt.figure()
#
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)
# axes.plot(x, y, 'r')
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('title')
#
# plt.show()
# coding=utf-8
# import numpy as np
# import matplotlib.pyplot as plt

# year = (1950, 1970, 1990, 2010)
# pop = (2.519, 3.692, 5.263, 6.972)
# # plt.fill_between(year,pop,0,color='green')
# # 折线图
# # plt.plot(year, pop)
# # s散点图
# # plt.scatter(year, pop)
# # values = np.linspace(0, 6, 10)
# values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
# # 柱形图
# plt.hist(values,bins=3)
# plt.xlabel("x")
# plt.ylabel('y')
# plt.title("title")
# # y轴刻度
# plt.yticks([0, 2, 4, 6, 8, 10])
#
# plt.show()

import matplotlib.pyplot as plt

labels = 'Frogs', 'Logs', 'Dogs', 'Hogs'  # 定义标签
sizes = [15, 30, 45, 10]  # 每一块的比例
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']  # 每一块的颜色
explode = (0, 0.1, 0, 0) #突出显示
#labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
#autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
#shadow，饼是否有阴影
#startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
#pctdistance，百分比的text离圆心的距离
#patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.savefig("bingtu.png")
plt.show()

