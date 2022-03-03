from flask import Flask, redirect, url_for,render_template,request
app =Flask(__name__,template_folder='../templates',static_folder='../static')

import sys
sys.path.append("../")
from controllers.users import add_user_request , get_password


@app.route('/')
def home():
   return render_template("index.html")

@app.route('/kayitol', methods=['POST', 'GET'])
def kayit_ol():
   
   if request.method == 'POST':
      isim = request.form.get('username') 
      email = request.form.get('email')
      sifre = request.form.get('password')  
      add_user_request(isim,email,sifre)
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
