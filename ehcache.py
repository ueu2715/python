import requests

url = 'http://130.10.7.123:8080/ecsvr/rest/sampleCache2/'
data = '1111111111'
res = requests.put(url+str(111),data=data)
print ('put data to ecsvr key is 111')
res = requests.get(url+'111')
print (res.text)
