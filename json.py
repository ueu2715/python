#-*- coding: utf-8 -*-
import random

f = open('point.json','w+')
isfirst = True
f.write('[')
for x in range(1,10):
	if isfirst:
		isfirst = False
	else:
		f.write(',')
	f.write(str(round(random.random(),3)))
f.write(']')
f.close()