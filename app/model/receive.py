#!/usr/bin/env python
import pika

import sqlite3


connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    decoded_string = body.decode("utf-8")
    listem=decoded_string.split()
    idd=listem[0][3:]
    x=listem[3]
    y=listem[6]
    date=listem[7][5:]+" "+listem[8]
    print("listem id :"+idd)
    print("listem x :"+x)
    print("listem y :"+y)
    print("listem date :"+date)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

