import sqlite3

conn=sqlite3.connect('musteri_hesap_bilgileri.db', check_same_thread=False)
print("Bağlantı gerçekleşti")

cursor=conn.cursor()
print("Cursor oluşturuldu")


import sys
sys.path.append("../")


def get_password(username):
   cursor.execute("""Select password From TBL_CUSTOMER Where username = ?""",(username))
   ilkveri=cursor.fetchone()
   print("ilk veri :"+ilkveri)
   return ilkveri

   
def get_username_id(username,password):
   cursor.execute("""Select customerId From TBL_CUSTOMER Where username = ? and password = ? """,(username,password))
   ilkveri=cursor.fetchone()
   print("ilk veri :"+str(ilkveri))
   return ilkveri

def get_all_username(username):
   cursor.execute("""Select username From TBL_CUSTOMER""")
   list_all=cursor.fetchall()
   for student in list_all:
         print("Tum db  veri :"+student)

   return list_all
   
def searchUsername(username):
   search_command="""Select * From Where username = '{}'"""
   cursor.execute(search_command.format(username))

   user=cursor.fetchone()

   conn.commit()
   conn.close()

   return user

def add_user(username,email,password):
   cursor.execute("""Insert into TBL_CUSTOMER (username,email,password) values (?,?,?) """,(username,email,password))
   conn.commit()
   conn.close()

def updateInfo(username,password,customer_id):
   update_command=""" Update TBL_CUSTOMER Set username = '{}',Set password = '{}' WHERE customerId={} """
   data=(username,password,customer_id)
   cursor.execute(update_command.format(data))
   print("Güncelleme basarılı")

   conn.commit()
   conn.close()

def deleteAccount(customer_id):
   delete_command=""" Delete From TBL_CUSTOMER WHERE customerId={} """
   data=(customer_id)
   cursor.execute(delete_command.format(data))
   print("Silme basarılı")
   conn.commit()
   conn.close()



def print_all():
   list_command=""" Select * From TBL_CUSTOMER """
   cursor.execute(list_command)
   list_all=cursor.fetchall()
   for student in list_all:
      print(student)

  
   conn.commit()
   conn.close()


