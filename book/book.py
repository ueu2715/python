#!/usr/bin/env python
#-*- coding: utf-8 -*-

import xlrd#读
import xlwt#写
from xlutils.copy import copy#保存
import requests#get请求
from xml.etree import ElementTree#xml解析
import re

data = xlrd.open_workbook('book.xls') # 打开xls文件
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows # 获取表的行数
wb = xlwt.Workbook()
sheet = wb.add_sheet('book')
row = 0

sheet.col(0).width = 20000
sheet.col(1).width = 3000
sheet.col(2).width = 5000
sheet.col(3).width = 5000
sheet.col(4).width = 5000
sheet.col(5).width = 5000
style = xlwt.easyxf('align: wrap on')

keys = ['A.','B.','C.','D.','E.','F.']
for i in range(nrows): # 循环逐行打印
	val = table.cell(i,0).value
	#if "单选题" in val or "多选题" in val or "判断题" in val:
	#	pass
	if "A." in val and "B." in val:
		ans = val.split()
		for x in ans:
			sheet.write(row-1,ans.index(x)+2 , x)
		continue
	flag = False
	for x in keys:
		if x in val:
			sheet.write(row-1, keys.index(x)+2, val,style)
			flag = True
			continue
	if flag:
		continue

	sheet.write(row, 0, val,style)
	#×√
	if '√' in val:
		sheet.write(row,1,'√')
	elif '×' in val:
	  	sheet.write(row,1,'×')
	else:
		m = re.match(r".*[\.]\s*(\w+)",val)
		if m:
			sheet.write(row,1,m.group(1))
	row += 1
wb.save('book1.xls')