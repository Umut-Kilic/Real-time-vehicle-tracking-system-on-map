from flask import Flask, redirect, url_for,render_template,request,flash,session , stream_with_context , Response
app =Flask(__name__,template_folder='../templates',static_folder='../static')
from gevent.pywsgi import WSGIServer
import json
import time
import sys
sys.path.append("../")
from controllers.users import   getHourlyCarRequest, add_user_request , get_password,is_avaiable_login,user_logout , get_30_min_request , getAllCars_30_min_request

app.secret_key = 'BAD_SECRET_KEY'





##############################
@app.route("/listen")
def listen():

  def respond_to_client():
    while True:
      global counter
      with open("color.txt", "r") as f:
        color = f.read()
        print("******************")
      if(color != "white"):
        print(counter)
        counter += 1
        _data = json.dumps({"color":color, "counter":counter})
        yield f"id: 1\ndata: {_data}\nevent: online\n\n"
      time.sleep(0.5)
  return Response(respond_to_client(), mimetype='text/event-stream')
  

@app.route('/tekaraba/<int:car_id>/<int:saat>')
def tekaraba(car_id,saat):
   car=getHourlyCarRequest(car_id,saat)
   return render_template('saatlikveri.html',saat=str(saat).upper(),car_id=car_id,car=car)



@app.route('/car/<int:car_id>/<int:saat>')
def saatsecimi(car_id,saat):

   return render_template("saatform.html",car_id=car_id)


@app.route('/logout')
def logout_request():
   user_logout()
   return redirect(url_for('home')) 

@app.route('/', methods=['POST', 'GET'])
def home():
   sessionuser=session.get('username', 'not set')
   sessionpassword=session.get('password','not set')
   
   if request.method == 'POST' or  (not sessionuser== 'not set' and not sessionpassword== 'not set') :
      isim = request.form.get('username','not set') 
      sifre = request.form.get('password','not set')
      
      
      
      if not sessionuser  =='not set' and not sessionpassword  =='not set':
         
         isim=str(sessionuser)
         sifre=str(sessionpassword)

      print(isim)
      print(sifre)
      if(is_avaiable_login(isim, sifre) ):
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




http_server = WSGIServer(("localhost", 80), app)
http_server.serve_forever()