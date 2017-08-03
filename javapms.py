# -*- coding: utf-8 -*-
import requests 
import zipfile
import configparser
import datetime
import os

configname = 'javapms.ini'
parse = configparser.ConfigParser()
parse.read(configname)

##get config
uri 		= parse.get('server','uri')
filename 	= parse.get('server','filename') 
path 		= parse.get('client','path')

##check dirs 
if not os.path.exists(path):
	os.makedirs(path)
##deal with config
if filename == '':
	filename = datetime.datetime.now().strftime('%Y%m%d') + '.zip'
	print ('get file name is ',filename)
if not uri.endswith('/'):
	uri += '/'
	print ('uri is ',uri)

tmpfile = '_javapms_tmp.zip'

##get zip file
print ('downloading with requests')
r = requests.get(uri+filename) 
with open(tmpfile, "wb") as code:
     code.write(r.content)

##extract zip file
print ('extracting zip file')
f = zipfile.ZipFile(tmpfile, 'r' )
f.extractall(path)
f.close()

print ('success!')