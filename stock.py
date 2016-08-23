#coding:gbk
import misc

def CreateWithFile(path):
	onestockinfo = misc.GetCsvList(path)
	onestockinfo.reverse()
	if not onestockinfo:
		print "文件有错", path
		return None
	return CStock(onestockinfo)

class CStock():
	def __init__(self, lDateInfo):
		oneday = lDateInfo[0]
		self.m_Code = oneday.get("股票代码")
		self.m_Name = oneday.get("股票名称")
		self.m_DateInfoList = lDateInfo #全部日线信息列表，必须以日期从前到后排序。不允许为空

#--------以下为对外接口-------------#
	def GetName(self):
		return self.m_Name

	def GetCode(self):
		return self.m_Code

	#是否是创业板
	def IsGEM(self):
		return self.m_Code.startswith("sz300")

	#返回最近一天的流通市值
	def GetFlowMarketValue(self):
		endindex = len(self.m_DateInfoList)-1
		lastdayinfo = self.m_DateInfoList[endindex]
		svalue = lastdayinfo.get("流通市值")
		return int(float(svalue))

	def GetMarketValue(self):
		endindex = len(self.m_DateInfoList) - 1
		lastdayinfo = self.m_DateInfoList[endindex]
		svalue = lastdayinfo.get("总市值")
		return int(float(svalue))

	def GetOneDayInfoAtIndex(self, idx):
		return self.m_DateInfoList[idx]

	def GetIPODay(self):
		firstdayinfo = self.m_DateInfoList[0]
		return firstdayinfo.get("交易日期")

	def GetTradeDayCount(self):
		return len(self.m_DateInfoList)

	def GetOpenPriceAtIndex(self, idx):
		onedayinfo = self.GetOneDayInfoAtIndex(idx)
		openprice = float(onedayinfo.get("开盘价"))
		return openprice

	def GetClosePriceAtIndex(self, idx):
		onedayinfo = self.GetOneDayInfoAtIndex(idx)
		closeprice =  float(onedayinfo.get("收盘价"))
		return closeprice