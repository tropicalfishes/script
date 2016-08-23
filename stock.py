#coding:gbk
import misc

def CreateWithFile(path):
	onestockinfo = misc.GetCsvList(path)
	onestockinfo.reverse()
	if not onestockinfo:
		print "�ļ��д�", path
		return None
	return CStock(onestockinfo)

class CStock():
	def __init__(self, lDateInfo):
		oneday = lDateInfo[0]
		self.m_Code = oneday.get("��Ʊ����")
		self.m_Name = oneday.get("��Ʊ����")
		self.m_DateInfoList = lDateInfo #ȫ��������Ϣ�б����������ڴ�ǰ�������򡣲�����Ϊ��

#--------����Ϊ����ӿ�-------------#
	def GetName(self):
		return self.m_Name

	def GetCode(self):
		return self.m_Code

	#�Ƿ��Ǵ�ҵ��
	def IsGEM(self):
		return self.m_Code.startswith("sz300")

	#�������һ�����ͨ��ֵ
	def GetFlowMarketValue(self):
		endindex = len(self.m_DateInfoList)-1
		lastdayinfo = self.m_DateInfoList[endindex]
		svalue = lastdayinfo.get("��ͨ��ֵ")
		return int(float(svalue))

	def GetMarketValue(self):
		endindex = len(self.m_DateInfoList) - 1
		lastdayinfo = self.m_DateInfoList[endindex]
		svalue = lastdayinfo.get("����ֵ")
		return int(float(svalue))

	def GetOneDayInfoAtIndex(self, idx):
		return self.m_DateInfoList[idx]

	def GetIPODay(self):
		firstdayinfo = self.m_DateInfoList[0]
		return firstdayinfo.get("��������")

	def GetTradeDayCount(self):
		return len(self.m_DateInfoList)

	def GetOpenPriceAtIndex(self, idx):
		onedayinfo = self.GetOneDayInfoAtIndex(idx)
		openprice = float(onedayinfo.get("���̼�"))
		return openprice

	def GetClosePriceAtIndex(self, idx):
		onedayinfo = self.GetOneDayInfoAtIndex(idx)
		closeprice =  float(onedayinfo.get("���̼�"))
		return closeprice