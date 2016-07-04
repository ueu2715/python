#/usr/bin/env python
#coding=utf8
 
import hashlib
import random
import requests#get请求
import json

appid = '20160612000023157'
secretKey = 'YJ9MDypbeAAHyaUw8ayQ'

#myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
myurl = 'http://fanyi.baidu.com/v2transapi'
q = 'python'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)
sign = appid+q+str(salt)+secretKey
m2 = hashlib.md5()   
m2.update(sign.encode('utf-8'))   
sign = m2.hexdigest()   
#param = {'q':q,'from':fromLang,'to':toLang,'salt':str(salt),'sign':sign,'appid':appid}
param = {'query':q,'transtype':'realtime','simple_means_flag':3,'from':fromLang,'to':toLang}
#myurl = myurl+'?appid='+appid+'&q='+q+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
 
try:
    result = requests.get(myurl,params=param)
    s = json.loads(result.text)#.encode('latin-1').decode('unicode_escape')
    symbols = s['dict_result']['simple_means']['symbols'][0]
    print (q)
    print ('英',symbols['ph_en'])
    print ('美',symbols['ph_am'])

    parts = symbols['parts']
    for p in parts:
    	print (p['part'],p['means'])
except Exception as e:
    print (e)

