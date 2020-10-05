#!/usr/bin/env python
import pika
import sys

import os
hostname= os.environ['RABBIT_HOST'] if 'RABBIT_HOST' in os.environ else 'localhost'

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=hostname))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print " [x] Sent %r" % (message,)
connection.close()
