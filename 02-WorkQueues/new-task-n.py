#!/usr/bin/env python3
import pika
import sys
import argparse

parser = argparse.ArgumentParser(
  description='Sends n hello world messages so the effect of not ' +
    'acknowledging messages can be seen.')
parser.add_argument('n', type=int, help='Number of messages to send') 
parser.add_argument('--message', type=str, default="Hello World!",
  help="Message to send.")
FLAGS = parser.parse_args()

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

for i in range(FLAGS.n):
  message = f"{i} {FLAGS.message}"
  channel.basic_publish(
      exchange='',
      routing_key='task_queue',
      body=message,
      properties=pika.BasicProperties(
          delivery_mode=2,  # make message persistent
      ))
  print(" [x] Sent %r" % message)
connection.close()
