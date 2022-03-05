#!/usr/bin/env python
import pika

import sqlite3


import firebase_admin 
from firebase_admin import credentials ,firestore

kimlik= credentials.Certificate('./key.json')
app=firebase_admin.initialize_app(kimlik)
db=firestore.client()


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
    document=db.collection("data").document(idd)

    document.update({
        
   date: {"x":x,
    "y":y
    }})

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

