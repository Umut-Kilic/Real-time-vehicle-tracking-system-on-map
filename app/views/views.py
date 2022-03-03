from flask import Flask, redirect, url_for,render_template,request,flash
app =Flask(__name__,template_folder='../templates',static_folder='../static')

import sys
sys.path.append("../")
from controllers.users import add_user_request , get_password,is_avaiable_login

app.secret_key = 'BAD_SECRET_KEY'


@app.route('/', methods=['POST', 'GET'])
def home():
   if request.method == 'POST':
      isim = request.form.get('username') 
      sifre = request.form.get('password')
      print("isim : "+isim)
      print("sifre : "+sifre)
      if(is_avaiable_login(isim, sifre)):

         return redirect(url_for('icerik')) 
       
   return render_template("index.html")

@app.route('/kayitol', methods=['POST', 'GET'])
def kayit_ol():
   
   if request.method == 'POST':
      isim = request.form.get('username') 
      email = request.form.get('email')
      sifre = request.form.get('password')  
      add_user_request(isim,email,sifre)
      return redirect(url_for('home'))
   flash("1221")
   return render_template("kayit.html")

@app.route('/icerik')
def icerik():
   return render_template("icerik.html")



if __name__ == '__main__':
   app.run()
