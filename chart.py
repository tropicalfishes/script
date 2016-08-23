#coding:gbk

from matplotlib import pyplot as plt

#根据横纵坐标数据列表显示散点图
def ShowScatterChart(xList, yList):
	plt.scatter(xList, yList)
	plt.show()
