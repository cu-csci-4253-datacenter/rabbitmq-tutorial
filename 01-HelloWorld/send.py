#!/usr/bin/env python3
import pika

import os
hostname= os.environ['RABBIT_HOST'] if 'RABBIT_HOST' in os.environ else 'localhost'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=hostname))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print( " [x] Sent 'Hello World!'" )
connection.close()
