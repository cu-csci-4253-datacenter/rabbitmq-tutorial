#!/usr/bin/env python3
import pika
import argparse

parser = argparse.ArgumentParser(
  description='Sends n hello world messages so the effect of not ' +
    'acknowledging messages can be seen.')
parser.add_argument('n', type=int, help='Number of messages to send') 
FLAGS = parser.parse_args()

import os
hostname= os.environ['RABBIT_HOST'] if 'RABBIT_HOST' in os.environ else 'localhost'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=hostname))
channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(FLAGS.n):
  channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Hello World!')
  print( " [x] Sent 'Hello World!'" )
connection.close()
