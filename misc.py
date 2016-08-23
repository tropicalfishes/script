#coding:gbk
import time

#��ȡcsv�ļ������Ե�һ��Ϊkeyֵ��ÿһ�е��ֵ��б�
def GetCsvList(csvpath):
	import csv
	f = file(csvpath, "rb")
	dictReader = csv.DictReader(f)
	lst = []
	for d in dictReader:
		lst.append(d)
	return lst

#����truerate==0.3�����аٷ�֮30�Ļ��᷵��True
def RandBool(truerate=0.5):
	import random
	fRand = random.random()
	if fRand < truerate:
		return True
	else:
		return False

#"2016-4-5"������ʽ�����ڷ��ص���0�����ı�׼ʱ��
def GetDate(sDate):
	dateList = sDate.split("-")
	if len(dateList) == 3:
		tTime = (int(dateList[0]), int(dateList[1]), int(dateList[2]), 0, 0, 0, 0, 0, 0)
		return int(time.mktime(tTime))
	else:
		print "����û��", sDate

#����׼ʱ�䷵�ض�Ӧ����
def TimeFormatDate(iTime):
	timeStruct = time.localtime(iTime)
	year, month, day = timeStruct.tm_year, timeStruct.tm_mon, timeStruct.tm_mday
	return "%s-%s_%s"%(year, month, day)

def PrintErr(s):
	print "[error]------------��%s" % s