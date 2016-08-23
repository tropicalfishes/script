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
		buyprice = float(buydate.get("开盘价"))
		sellprice = float(selldate.get("收盘价"))
		profitrate = (sellprice-buyprice)/buyprice*100
		return profitrate
	else:
		return 0

def GetProfitRate2(dataList, i):
	if len(dataList) > i+2:
		buydate = dataList[i]
		selldate = dataList[i+2]
		buyprice = float(buydate.get("收盘价"))
		sellprice = float(selldate.get("收盘价"))
		profitrate = (sellprice-buyprice)/buyprice*100
		return profitrate
	else:
		return 0

def GetProfitRate3(dataList, i):
	if len(dataList) > i+2:
		tdate = dataList[i]
		buydate = dataList[i+1]
		selldate = dataList[i+2]
		buyprice = float(tdate.get("收盘价"))
		lowprice = float(buydate.get("最低价"))
		if lowprice > buyprice:
			return 0
		sellprice = float(selldate.get("收盘价"))
		profitrate = (sellprice-buyprice)/buyprice*100
		return profitrate
	else:
		return 0

#把lst的数据转成[1,2,3,4]形式
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
	print "剔除重合后日期数", idx-1
#	print "打印转换数据"
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
	print "日期转换完后", idx
	return finalDate, finalProfit

def TransDate2String(dateList):
	finalList = []
	for idx in dateList:
		iDate = g_Idx2Date.get(idx)
		if not iDate:
			print "没有这个idx对应的日期，转换有问题"
			continue
		sDate = misc.TimeFormatDate(iDate)
		finalList.append(sDate)
	return finalList

def DrawPointImage(dateList, profitList):
	from matplotlib import pyplot as plt
	dateList = TransList(dateList)
	print "第一种转换后的日期数：", len(dateList), len(profitList)
	finalDate, finalProfit = TransDateProfitList()
#	sFinalDateList = TransDate2String(finalDate)
	plt.scatter(finalDate, finalProfit)
	print "最后", g_Idx2Date
	plt.show()

def PrintDateData():
	print "现在打印日期数据"
	for k, v in g_ProfitDict.items():
		print "%-20s%-5s"%(k, v)
	
Main()