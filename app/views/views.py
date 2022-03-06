from flask import Flask, redirect, url_for,render_template,request,flash
app =Flask(__name__,template_folder='../templates',static_folder='../static')

import sys
sys.path.append("../")
from controllers.users import add_user_request , get_password,is_avaiable_login,user_logout , get_30_min_request

app.secret_key = 'BAD_SECRET_KEY'



@app.route('/logout')
def logout_request():
   user_logout()
   return redirect(url_for('home')) 

@app.route('/', methods=['POST', 'GET'])
def home():
   if request.method == 'POST':
      isim = request.form.get('username') 
      sifre = request.form.get('password')

      car=get_30_min_request(1)
      if(is_avaiable_login(isim, sifre)):

         return render_template('icerik.html',isim=isim.upper(),car=car) 
       
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


@app.route('/icerik', methods=['POST', 'GET'])
def icerik():
   if request.method == 'GET':
      get_30_min_request(1)
      return render_template("icerik.html",isim=username )
   else:
      return render_template("icerik.html")
     
  



if __name__ == '__main__':
   app.run(debug=True)