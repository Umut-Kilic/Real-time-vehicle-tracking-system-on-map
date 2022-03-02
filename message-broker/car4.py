#!/usr/bin/env python
import pika
import sys
import time
import csv
import pandas as pd
sayac=0


#allCars.csv
#carid - > 1

col_Names=["date", "x", "y", "carid"]
data= pd.read_csv("allCars.csv",names=col_Names)
car1 = data[data["carid"] ==4]
x,y = car1.x , car1.y
index=500

while True:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs', exchange_type='fanout')
    
    message= "ID : 4 :"+ str(  x[500+sayac]) +" "+ str( y[500+sayac]  )
    channel.basic_publish(exchange='logs', routing_key='123', body=message)
    print(" [x] Sent %r" % message)
    connection.close()
    sayac=sayac+1
    time.sleep(0.25)