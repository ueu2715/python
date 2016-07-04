#-*- coding: UTF-8 -*-

file = open(r"a.txt")
f = open('b.txt','w+')

print (f.newlines)
for line in file:
	linet = line
	line = line.encode('unicode-escape').decode('utf-8')
	line = line.replace('\\n','')
	print (line)
	f.write(linet)
	f.write('='+line+'\n')
	
f.close()
file.close()