#coding:gbk
import module


class KdjModule(module.ModuleBase):
	MAX_FLOW_VALUE = 25 * 100000000
	MAX_KDJ_K = 20
	HOLD_DAY_CNT = 2 #��������

	#�����Ƿ��������
	def IsStockMatch(self, oStock):
		bGem =  oStock.IsGEM()
		iFlowValue = oStock.GetFlowMarketValue()
		return bGem and iFlowValue < self.MAX_FLOW_VALUE

	#���ɵ����Ƿ���������
	def IsDayMatch(self, dOneDayInfo):
		bGoldCross = dOneDayInfo.get("KDJ_�������") == "���"
		fKdj = float(dOneDayInfo.get("KDJ_K"))
		return bGoldCross and fKdj < self.MAX_KDJ_K

	#��ȡ���������ģ�͵�����
	def GetOneStockProfit(self, oStock):
		if not self.IsStockMatch(oStock):
			return 0
		profit = 0
		daycnt = oStock.GetTradeDayCount()
		for dayidx in xrange(daycnt-self.HOLD_DAY_CNT):
			dOneDayInfo = oStock.GetOneDayInfoAtIndex(dayidx)
			if self.IsDayMatch(dOneDayInfo):
				onedayprofit = self.GetOneMatchProfit(oStock, dayidx)
				print "��������", dOneDayInfo.get("��Ʊ����"), dOneDayInfo.get("��������"), onedayprofit
				profit += onedayprofit
		return profit

	#��ȡ�����ڷ���ģ�͵�ĳһ�������
	def GetOneMatchProfit(self, oStock, dayidx):
		buyprice = oStock.GetClosePriceAtIndex(dayidx)
		sellprice = oStock.GetClosePriceAtIndex(dayidx+self.HOLD_DAY_CNT)
		return (sellprice - buyprice)/buyprice*100

