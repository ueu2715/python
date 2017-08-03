#!/usr/bin/env python  
import pika  
import sys  
  
creds_broker = pika.PlainCredentials("rjsjb", "rjsjb123")  

parameters = pika.ConnectionParameters( "192.168.159.191",  
                                             port=5672,  
                                             virtual_host="/rjsjb",  
                                             credentials=creds_broker)
  
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
  
channel.exchange_declare(exchange='logs',  
                         type='fanout')  
  
message = ' '.join(sys.argv[1:]) or "info: Hello World!1111111"  
channel.basic_publish(exchange='logs',  
                      routing_key='',  
                      body=message)  
print " [x] Sent %r" % (message,)  
connection.close()  