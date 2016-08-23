#coding:gbk
import module


class KdjModule(module.ModuleBase):
	MAX_FLOW_VALUE = 25 * 100000000
	MAX_KDJ_K = 20
	HOLD_DAY_CNT = 2 #持有天数

	#个股是否符合条件
	def IsStockMatch(self, oStock):
		bGem =  oStock.IsGEM()
		iFlowValue = oStock.GetFlowMarketValue()
		return bGem and iFlowValue < self.MAX_FLOW_VALUE

	#个股当天是否满足条件
	def IsDayMatch(self, dOneDayInfo):
		bGoldCross = dOneDayInfo.get("KDJ_金叉死叉") == "金叉"
		fKdj = float(dOneDayInfo.get("KDJ_K"))
		return bGoldCross and fKdj < self.MAX_KDJ_K

	#获取个股在这个模型的收益
	def GetOneStockProfit(self, oStock):
		if not self.IsStockMatch(oStock):
			return 0
		profit = 0
		daycnt = oStock.GetTradeDayCount()
		for dayidx in xrange(daycnt-self.HOLD_DAY_CNT):
			dOneDayInfo = oStock.GetOneDayInfoAtIndex(dayidx)
			if self.IsDayMatch(dOneDayInfo):
				onedayprofit = self.GetOneMatchProfit(oStock, dayidx)
				print "这天满足", dOneDayInfo.get("股票代码"), dOneDayInfo.get("交易日期"), onedayprofit
				profit += onedayprofit
		return profit

	#获取个股在符合模型的某一天的收益
	def GetOneMatchProfit(self, oStock, dayidx):
		buyprice = oStock.GetClosePriceAtIndex(dayidx)
		sellprice = oStock.GetClosePriceAtIndex(dayidx+self.HOLD_DAY_CNT)
		return (sellprice - buyprice)/buyprice*100

