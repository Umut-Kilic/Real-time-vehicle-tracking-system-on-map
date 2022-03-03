from flask import Flask, redirect, url_for,render_template,request
app =Flask(__name__,template_folder='../templates',static_folder='../static')


import sqlite3

conn=sqlite3.connect('musteri_hesap_bilgileri.db', check_same_thread=False)
print("Bağlantı gerçekleşti")

cursor=conn.cursor()
print("Cursor oluşturuldu")

def searchUsername(username):
   search_command="""Select * From Where username = '{}'"""
   cursor.execute(search_command.format(username))

   user=cursor.fetchone()

   conn.commit()
   conn.close()

   return user

def insertData(username,email,password):
   
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



@app.route('/')
def home():
   return render_template("index.html")

@app.route('/kayitol', methods=['POST', 'GET'])
def kayit_ol():
   
   if request.method == 'POST':
      isim = request.form.get('username') 
      email = request.form.get('email')
      sifre = request.form.get('password')  
      insertData(isim,email,sifre)

      return redirect(url_for('home'))
   return render_template("kayit.html")

@app.route('/icerik')
def icerik():
   return render_template("kayit.html")

@app.route('/db')
def db():
   
     """ return render_template("veri.html",isim=isim,email=email,sifre=sifre)

   else:
      return render_template("veri.html",hata="Formdan veri gelmedi!")"""

if __name__ == '__main__':
   app.run()
