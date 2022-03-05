#!/usr/bin/env python
import pika
import sys
import time
import csv
import pandas as pd
import sqlite3
from model.users import getOnlineUsersCar
import pprint
col_Names=["date", "x", "y", "carid"]
data= pd.read_csv("allCars.csv",names=col_Names)

def otuzyolla(index,car,id):
    for i in range(30):
        currentindex=index+i
        date=car.values[currentindex][0]
        x=car.values[currentindex][1]
        y=car.values[currentindex][2]
        

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

      
        channel = connection.channel()
        channel.exchange_declare(exchange='logs', exchange_type='fanout')
        message=  "id=" + str(id) + "  x : " + str(x) +"  y : " + str(y) + " date:" + str(date)
        channel.basic_publish(exchange='logs', routing_key='123', body=message)
        print(" [x] Sent %r" % message)
        connection.close()
     
        time.sleep(0.02)
        



sayac=0
conn=sqlite3.connect('views/musteri_hesap_bilgileri.db', check_same_thread=False)
cursor=conn.cursor()

liste=getOnlineUsersCar(cursor)


#allCars.csv
#carid - > 1





otuzluk=[]


while True:
    
    for carid in liste:
        car = data[ (data['carid'] ==carid[0])]
        x,y,date = car.x , car.y , car.date
 
        if   not  otuzluk.count(carid[0]) >=1:
            otuzyolla(0,car,carid[0])
            otuzluk.append(carid[0])
            
        
    
