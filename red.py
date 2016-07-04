#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 读取excel第一列单词，生成音标，翻译
# 
import xlrd#读
import xlwt#写
from xlutils.copy import copy#保存
import requests#get请求
from xml.etree import ElementTree#xml解析
data = xlrd.open_workbook('red.xls') # 打开xls文件
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows # 获取表的行数
wb = copy(data)
sheet = wb.get_sheet(0)
#列宽
sheet.col(0).width = 5000
sheet.col(1).width = 5000
sheet.col(2).width = 15000
#自动换行
style = xlwt.easyxf('align: wrap on')
for i in range(nrows): # 循环逐行打印
    if i == 0: # 跳过第一行
        continue

    key = table.cell(i,0).value
    param = {'q':key,'doctype':'xml'}
    url = 'http://dict.youdao.com/search' 
    result = requests.get(url,params=param)
    xml = result.text
    root = ElementTree.fromstring(xml)
    #音标
    yb = root.find('phonetic-symbol').text
    sheet.write(i, 1, yb)
    #翻译
    trans = ''
    count = 0
    for elem in root.iterfind('custom-translation/translation'):
        if count > 0:
            trans += '\r\n'
        trans = trans+elem.findtext('content')
        count = count + 1
    sheet.write(i, 2, trans,style)
    print (key,'---',yb)

wb.save('red.xls')
