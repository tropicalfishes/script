#coding:gbk
import misc

class ModuleBase():

	#ÿ��ģ�ͱ�����д�������
	def GetOneStockProfit(self, oStock):
		return 0

	def GetOneStockProfitFromFile(self, csvpath):
		import stock
		oStock = stock.CreateWithFile(csvpath)
		if oStock:
			profit = self.GetOneStockProfit(oStock)
#			print "�������棺%s, %s, %s" % (oStock.m_Code, oStock.m_Name, round(profit, 2))
			return profit
		else:
			misc.PrintErr("һ����Ʊ���󴴽�����%s" % csvpath)
			return 0

	#��ȡһ��Ŀ¼�µĹ�Ʊ������
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
