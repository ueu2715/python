#!/usr/bin/env python  
import pika  

creds_broker = pika.PlainCredentials("rjsjb", "rjsjb123")  

parameters = pika.ConnectionParameters( "192.168.159.191",  
                                             port=5672,  
                                             virtual_host="/rjsjb",  
                                             credentials=creds_broker)
  

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
  
channel.queue_declare(queue='hello')  
  
channel.basic_publish(exchange='',  
                      routing_key='hello',  
                      body='Hello World!333')  
print " [x] Sent 'Hello World!'"  
connection.close()  