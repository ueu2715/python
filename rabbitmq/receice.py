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
    
print ' [*] Waiting for messages. To exit press CTRL+C'    
    
def callback(ch, method, properties, body):    
    print " [x] Received %r" % (body,)    
    
channel.basic_consume(callback,    
                      queue='hello',    
                      no_ack=True)    
    
channel.start_consuming()    