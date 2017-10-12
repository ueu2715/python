#!/usr/bin/python
#encoding: utf-8

import re
import threading
import os
import time
import threadpool


ok = []
fail = []

def ping(host):
    '''ping 1次指定地址'''
    import subprocess,traceback, platform
    if platform.system()=='Windows':
        res = os.system('ping -n 1 -w 1 %s'%host)
    else:
        res = 'ping -c %d %s'%(1,host)
    if res:
    	#print 'ping %s is fail'%host
    	fail.append(host)
    else:
    	#print 'ping %s is ok'%host
    	ok.append(host)


pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
ips = {}
count = 0

f = open('hosts','r')
for line in f.readlines():
	match = pattern.match(line)
	count = count + 1
	if match:
		#print match.group()
		ips[match.group()] = line

print len(ips),count



threads = []

for ip in ips:
	#print ping(ip)
	t = threading.Thread(target=ping,args=(ip,))
	t.deamon = True
	threads.append(t)

#for t in threads:
#        t.start()
pool = threadpool.ThreadPool(100)
requests = threadpool.makeRequests(ping,ips)
[pool.putRequest(req) for req in requests]
pool.wait() 
#for i in ok:
#	print ips[i]
