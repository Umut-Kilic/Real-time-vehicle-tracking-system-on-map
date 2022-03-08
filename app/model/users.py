import sys
from turtle import pos
sys.path.append("../")

import sqlite3
import firebase_admin 
from firebase_admin import credentials ,firestore
from pprint import pprint
kimlik= credentials.Certificate('../key.json')
app=firebase_admin.initialize_app(kimlik)
db=firestore.client()



def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def bubblesort(array,temp1,temp2,temp3):
   n = len(array)-1
   for i in range(0, len(array)):
        for j in range(0, n):
            if array[j] > array[j+1]:
                swap(array, j+1, j)
                swap(temp1, j+1, j)
                swap(temp3, j+1, j)
                swap(temp2, j+1, j)
        n -= 1
   return array ,temp1,temp2,temp3


conn=sqlite3.connect('../views/musteri_hesap_bilgileri.db', check_same_thread=False)


cursor=conn.cursor()



def get_car_for_last_30_min(id):
   x_list=[]
   y_list=[]
   date_list=[]
   doc_ref = db.collection(u'data').document(str(id))
   
   doc = doc_ref.get()._data

   for value, date in doc.items():
     x_list.append(doc[value]['x'])
     y_list.append(doc[value]['y'])
     date_list.append(value)
   return x_list , y_list , date_list 
   
get_car_for_last_30_min(1)

def get_password(username):
   cursor.execute("""Select password From TBL_CUSTOMER Where username = ?""",(username))
   ilkveri=cursor.fetchone()
 
   return ilkveri[0]

   
def get_username_id(username):
   get_id_command="""Select customerId From TBL_CUSTOMER Where username = '{}' """
   cursor.execute(get_id_command.format(username))
   ilkveri=cursor.fetchone()
   if(ilkveri!=None):
      return ilkveri[0]
   else:
      return None  

def get_customer_id(username,password):
   cursor.execute("""Select customerId From TBL_CUSTOMER Where username = ? and password = ? """,(username,password))
   ilkveri=cursor.fetchone()
   if(ilkveri!=None):
      return ilkveri[0]
   else:
      return None

def get_all_username(username):
   cursor.execute("""Select username From TBL_CUSTOMER""")
   list_all=cursor.fetchall()


   return list_all
   
def searchUsername(username):
   search_command="""Select * From Where username = '{}'"""
   cursor.execute(search_command.format(username))

   user=cursor.fetchone()

   conn.commit()
   #conn.close()

   return user

def add_user(username,email,password):
   cursor.execute("""Insert into TBL_CUSTOMER (username,email,password,failed_count) values (?,?,?,0) """,(username,email,password))
   conn.commit()
   #conn.close()

def resetFailedCount(customer_id):
   update_command=""" Update TBL_CUSTOMER Set failed_count=0 WHERE customerId={} """
   data=(customer_id)
   cursor.execute(update_command.format(data))

   conn.commit()
   #conn.close()

def is_online(id,boolean):
   if(id!=None):
      if(boolean):
         update_command=""" Update TBL_CUSTOMER Set is_online="True" WHERE customerId={} """
         data=(id)
         cursor.execute(update_command.format(data))
      else:
         update_command=""" Update TBL_CUSTOMER Set is_online="False" WHERE customerId={} """
         data=(id)
         cursor.execute(update_command.format(data))
      

def updateFailedCount(customer_id):

   if(customer_id!=None):
    
      update_command=""" Update TBL_CUSTOMER Set failed_count=failed_count+1 WHERE customerId={} """
      cursor.execute(update_command.format(customer_id))
      sql_command="""Select failed_count From TBL_CUSTOMER WHERE customerId={} """
      cursor.execute(sql_command.format(customer_id))
      hatali_giris_sayisi=cursor.fetchone()
     
      return hatali_giris_sayisi[0]


      conn.commit()
      #conn.close()
   

def deleteAccount(customer_id):
   if(customer_id!=None):
      delete_command=""" Delete From TBL_CUSTOMER WHERE customerId={} """
      data=(customer_id)
      cursor.execute(delete_command.format(data))
      conn.commit()
      #conn.close()



def print_all():
   list_command=""" Select * From TBL_CUSTOMER """
   cursor.execute(list_command)
   list_all=cursor.fetchall()
  

   conn.commit()
   #conn.close()


def setLoginTime(customer_id,time):
   cursor.execute("""Insert into TBL_CUSTOMER_ACTIVITY (customer_id,kind_of_activity,time) values (?,'Login',?) """,(customer_id,time))
   conn.commit()
   #conn.close()
   

def setLogoutTime(customer_id,time):
   cursor.execute("""Insert into TBL_CUSTOMER_ACTIVITY (customer_id,kind_of_activity,time) values (?,'Logout',?) """,(customer_id,time))
   conn.commit()
   #conn.close()

def getOnlineUsersCar(cursor):
   cursor.execute(""" Select DISTINCT(CarId) From TBL_CUSTOMER,TBL_CUSTOMER_CAR Where TBL_CUSTOMER.is_online='True' """)
   list_all=cursor.fetchall()
   conn.commit()
   return list_all


def getCarsIdFromUserId(id):
   
   search_command=""" Select DISTINCT(CarId) From TBL_CUSTOMER_CAR Where customerId = '{}'"""
 

   cursor.execute(search_command.format(id))

   carids=cursor.fetchall()
  
   conn.commit()
   car_id_list=[]
   for carid in carids:
      car_id_list.append(carid[0])

   print(car_id_list)
   return car_id_list

from datetime import datetime 
import time
def get_car_position_hourly(car_id,hourr): 
   x_list=[]
   y_list=[]
   date_list=[]
   total_minute_list=[]
   doc_ref = db.collection(u'ALLCARS').document(str(car_id))

   doc = doc_ref.get()._data
   
   for date, position in doc.items():
      minute = str(date[-2:]) 
      hour = str(date [-5:-3])
   
      if str(minute [0])==" ":
         minute=minute[1]
      if str(hour [0])==" ":
         hour=hour[1]
     
      total_min=  int(hour) * 60 +  int(minute)
      total_minute_list.append(total_min)

      x_list.append(position['x'])
      y_list.append(position['y'])
      date_list.append(date)
   total_minute_list,x_list,x_list,date_list=bubblesort(total_minute_list,x_list,x_list,date_list)
   total_minute_list =total_minute_list + total_minute_list
   x_list =x_list + x_list
   y_list =y_list + y_list
   date_list =date_list + date_list
   now = datetime.now()
   now_total_minute=now.hour*60 + now.minute
   maxminuteindex=total_minute_list.index(now_total_minute,1440)
   minminuteindex= maxminuteindex- int(hourr) * 60 

   x_list=x_list[minminuteindex:maxminuteindex]
   
   date_list=date_list[minminuteindex:maxminuteindex]
   y_list=y_list[minminuteindex:maxminuteindex]
   #atmayı unutmuşum
   return date_list , x_list , y_list
   
   
   #ELIMIXDEKI MAXSİMUM INDEX == NEREDEN GERIYE DOGRU SAYILACAK
   
   #print(qq)
   
   #total_min_list kücükten büyüge sırala: index değişirken x list , y list  ,  date list değiştir.
   
   
