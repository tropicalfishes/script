#coding:gbk
import misc

class ModuleBase():

	#每个模型必须重写这个函数
	def GetOneStockProfit(self, oStock):
		return 0

	def GetOneStockProfitFromFile(self, csvpath):
		import stock
		oStock = stock.CreateWithFile(csvpath)
		if oStock:
			profit = self.GetOneStockProfit(oStock)
#			print "个股收益：%s, %s, %s" % (oStock.m_Code, oStock.m_Name, round(profit, 2))
			return profit
		else:
			misc.PrintErr("一个股票对象创建出错：%s" % csvpath)
			return 0

	#获取一个目录下的股票的收益
	def GetProfitFromDir(self, dir, shuffle=True):
		import os, random
		profit = 0
		filelist = os.listdir(dir)
		if shuffle:
			random.shuffle(filelist)
		for filename in filelist:
			filepath = os.path.join(dir, filename)
			if not os.path.isfile(filepath):
				continue
			oneStockProfit = self.GetOneStockProfitFromFile(filepath)
			profit += oneStockProfit
		return profit
