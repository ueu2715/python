#!/usr/bin/env python  
import pika  
  
creds_broker = pika.PlainCredentials("rjsjb", "rjsjb123")  

parameters = pika.ConnectionParameters( "192.168.159.191",  
                                             port=5672,  
                                             virtual_host="/rjsjb",  
                                             credentials=creds_broker)
  
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
  
channel.exchange_declare(exchange='logs',  
                         type='fanout')  
  
result = channel.queue_declare(exclusive=True)  
queue_name = result.method.queue  
  
channel.queue_bind(exchange='logs',  
                   queue=queue_name)  
  
print ' [*] Waiting for logs. To exit press CTRL+C'  
  
def callback(ch, method, properties, body):  
    print " [x] %r" % (body,)  
  
channel.basic_consume(callback,  
                      queue=queue_name,  
                      no_ack=True)  
  
channel.start_consuming()  