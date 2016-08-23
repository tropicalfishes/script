#coding:gbk
import os
import random
import time
import csv
import misc

UP_DIR = "../overview-data-sz"


g_DateList = []
g_ProfitList = []
g_ProfitDict = {}
g_DateProfitList = []
g_Idx2Date = {}

def Main():
	import kdjmodule
	oKdjModule = kdjmodule.KdjModule()
	print oKdjModule.GetProfitFromDir(UP_DIR)

def GetProfitRate(dataList, i):
	if len(dataList) > i+2:
		buydate = dataList[i+1]
		selldate = dataList[i+2]
		buyprice = float(buydate.get("���̼�"))
		sellprice = float(selldate.get("���̼�"))
		profitrate = (sellprice-buyprice)/buyprice*100
		return profitrate
	else:
		return 0

def GetProfitRate2(dataList, i):
	if len(dataList) > i+2:
		buydate = dataList[i]
		selldate = dataList[i+2]
		buyprice = float(buydate.get("���̼�"))
		sellprice = float(selldate.get("���̼�"))
		profitrate = (sellprice-buyprice)/buyprice*100
		return profitrate
	else:
		return 0

def GetProfitRate3(dataList, i):
	if len(dataList) > i+2:
		tdate = dataList[i]
		buydate = dataList[i+1]
		selldate = dataList[i+2]
		buyprice = float(tdate.get("���̼�"))
		lowprice = float(buydate.get("��ͼ�"))
		if lowprice > buyprice:
			return 0
		sellprice = float(selldate.get("���̼�"))
		profitrate = (sellprice-buyprice)/buyprice*100
		return profitrate
	else:
		return 0

#��lst������ת��[1,2,3,4]��ʽ
def TransList(lst):
	finallst = []
	listvaluedict = {}
	idx = 1
	for i in lst:
		if i in listvaluedict:
			value = listvaluedict.get(i)
			finallst.append(value)
		else:
			value = idx
			listvaluedict[i] = value
			finallst.append(value)
			idx += 1
	print "�޳��غϺ�������", idx-1
#	print "��ӡת������"
#	for k, v in listvaluedict.items():
#		print time.ctime(k), v
	return finallst

def TransDateProfitList():
	tempList = g_DateProfitList[:]
	tempList.sort()
	idx = 0
	lastDate = None
	finalDate = []
	finalProfit = []
	for tDateProfit in tempList:
		iDate, profit = tDateProfit
		if iDate != lastDate:
			idx += 1
			lastDate = iDate
			g_Idx2Date[idx] = misc.TimeFormatDate(iDate)
		finalDate.append(idx)
		finalProfit.append(profit)
	print "����ת�����", idx
	return finalDate, finalProfit

def TransDate2String(dateList):
	finalList = []
	for idx in dateList:
		iDate = g_Idx2Date.get(idx)
		if not iDate:
			print "û�����idx��Ӧ�����ڣ�ת��������"
			continue
		sDate = misc.TimeFormatDate(iDate)
		finalList.append(sDate)
	return finalList

def DrawPointImage(dateList, profitList):
	from matplotlib import pyplot as plt
	dateList = TransList(dateList)
	print "��һ��ת�������������", len(dateList), len(profitList)
	finalDate, finalProfit = TransDateProfitList()
#	sFinalDateList = TransDate2String(finalDate)
	plt.scatter(finalDate, finalProfit)
	print "���", g_Idx2Date
	plt.show()

def PrintDateData():
	print "���ڴ�ӡ��������"
	for k, v in g_ProfitDict.items():
		print "%-20s%-5s"%(k, v)
	
Main()