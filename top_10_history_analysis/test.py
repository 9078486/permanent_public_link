# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
import csv
#matplotlib.use('pdf')
import matplotlib.pyplot as plt


# 从top10_raw_data.csv中读取数据
decline_percentage = np.zeros(0)
currency_name_list = []

with open('top10_raw_data.csv', 'r', encoding='utf-8') as f:
	reader = csv.reader(f)
	for line in reader:
		decline_percentage = np.append(decline_percentage, np.array(float(line[6])))
		currency_name_list.append(line[0])

print(decline_percentage)
print(currency_name_list)
#print(np.mean(decline_percentage))
#decline_percentage.sort()
#print(decline_percentage)
# 绘制波动率箱体图
plt.subplot(2, 1, 1)
plt.boxplot(decline_percentage, sym='g+',
	showmeans=True, patch_artist=True, vert=False, meanline=False)
plt.subplot(2, 1, 2)
plt.grid(axis='y')
plt.plot(decline_percentage)
#plt.grid(axis='y')
#print(np.percentile(decline_percentage, [25, 50, 75]))

#plt.savefig('decline_percentage')
plt.show()
#print(sorted(decline_percentage))


#print((0.166009827 + 0.319165379)/2)

