#coding:gbk
import time

#读取csv文件返回以第一行为key值，每一行的字典列表
def GetCsvList(csvpath):
	import csv
	f = file(csvpath, "rb")
	dictReader = csv.DictReader(f)
	lst = []
	for d in dictReader:
		lst.append(d)
	return lst

#比如truerate==0.3，则有百分之30的机会返回True
def RandBool(truerate=0.5):
	import random
	fRand = random.random()
	if fRand < truerate:
		return True
	else:
		return False

#"2016-4-5"这种形式的日期返回当天0点整的标准时间
def GetDate(sDate):
	dateList = sDate.split("-")
	if len(dateList) == 3:
		tTime = (int(dateList[0]), int(dateList[1]), int(dateList[2]), 0, 0, 0, 0, 0, 0)
		return int(time.mktime(tTime))
	else:
		print "这天没有", sDate

#将标准时间返回对应日期
def TimeFormatDate(iTime):
	timeStruct = time.localtime(iTime)
	year, month, day = timeStruct.tm_year, timeStruct.tm_mon, timeStruct.tm_mday
	return "%s-%s_%s"%(year, month, day)

def PrintErr(s):
	print "[error]------------：%s" % s