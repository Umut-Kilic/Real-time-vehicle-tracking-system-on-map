#!/usr/bin/env python
import pika
import sys
import time
import csv
import pandas as pd
import sqlite3
from model.users import getOnlineUsersCar

sayac=0
conn=sqlite3.connect('views/musteri_hesap_bilgileri.db', check_same_thread=False)
print("Bağlantı gerçekleşti")
cursor=conn.cursor()
print("Cursor oluşturuldu")

liste=getOnlineUsersCar(cursor)
print(liste)

#allCars.csv
#carid - > 1

col_Names=["date", "x", "y", "carid"]
data= pd.read_csv("allCars.csv",names=col_Names)

car1 = data[ (data['carid'] ==10 )]
x,y = car1.x , car1.y
index=500

while True:
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='fanout')
    message= "1221"
    channel.basic_publish(exchange='logs', routing_key='123', body=message)
    #print(" [x] Sent %r" % message)
    connection.close()
    sayac=sayac+1
    time.sleep(0.25)