from flask import Flask, redirect, url_for,render_template,request,flash
app =Flask(__name__,template_folder='../templates',static_folder='../static')

import sys
sys.path.append("../")
from controllers.users import add_user_request , get_password,is_avaiable_login,user_logout , get_30_min_request , getAllCars_30_min_request

app.secret_key = 'BAD_SECRET_KEY'



@app.route('/car/<int:car_id>')
def one_car(car_id):
   
   return str(car_id)


@app.route('/logout')
def logout_request():
   user_logout()
   return redirect(url_for('home')) 

@app.route('/', methods=['POST', 'GET'])
def home():
   if request.method == 'POST':
      isim = request.form.get('username') 
      sifre = request.form.get('password')

      
      if(is_avaiable_login(isim, sifre)):
         cars=getAllCars_30_min_request(5)

         return render_template('icerik.html',isim=isim.upper(),cars=cars) 
       
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


if __name__ == '__main__':
   app.run(debug=True)