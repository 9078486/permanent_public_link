# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import csv

# ----------Part 1----------
# 数据获取和处理

# 创建空列表用于存储价格和日期数据
date_list = []
price_list = []

# 从csv文件中读取价格和日期数据
with open('BTC-USD.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		date = row[0]
		date_list.append(date)
		price = float(row[4])
		price_list.append(price)

# 获取比特币历史最高价及最高价日期的索引
historic_highest_price = np.max(price_list)
max_date = np.argmax(price_list)

# ----------Part 2----------
# 图表绘制

# 建立并设置画布大小
plt.figure(figsize=[20, 6])

# 让图标中可以显示中文
mpl.rcParams['font.sans-serif'] = ['SimHei']  

# 绘制折线图，并设置标签为'BTC'
plt.plot(date_list, price_list, label="BTC")

# 由于X轴日期数据过多，无法全部显示
# 所以设置为间隔150天标注一个价格 
plt.xticks(np.arange(0, len(date_list), 150), 
	[date_list[i] for i in np.arange(0, len(date_list), 150)],
	rotation=15) 

# 格式设置
plt.title("Bitcoin Price")           # 设置图标标题
plt.xlabel("Date")                   # 设置x轴标签
plt.ylabel("Price\nUSD")             # 设置y轴标签
plt.grid()                           # 添加网格线

ax = plt.gca()
ax.spines["right"].set_color('none') # 隐藏图表右边框
ax.spines["top"].set_color('none')   # 隐藏图表上边框

# 在图标中标注历史最高价
plt.annotate(
			'历史最高价\nUSD 19497.40',  
			xy=(max_date, historic_highest_price), 
			xytext=(max_date + 150, historic_highest_price + 150),
			arrowprops=dict(arrowstyle='->')
			)

# 显示图表
plt.show()




