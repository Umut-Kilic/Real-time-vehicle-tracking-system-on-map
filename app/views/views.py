from flask import Flask, redirect, url_for,render_template,request,flash
app =Flask(__name__,template_folder='../templates',static_folder='../static')

import sys
sys.path.append("../")
from controllers.users import add_user_request , get_password,is_avaiable_login,user_logout

app.secret_key = 'BAD_SECRET_KEY'


class School:
    def __init__(self, key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

schools = (
    School('hv',      'Happy Valley Elementary',   37.9045286, -122.1445772),
    School('stanley', 'Stanley Middle',            37.8884474, -122.1155922),
    School('wci',     'Walnut Creek Intermediate', 37.9093673, -122.0580063)
)
schools_by_key = {school.key: school for school in schools}



@app.route("/<school_code>")
def show_school(school_code):
    school = schools_by_key.get(school_code)
    if school:
        return render_template('map.html', school=school)
    else:
         return render_template('map.html', school=school)



@app.route('/logout')
def logout_request():
   user_logout()
   return redirect(url_for('home')) 

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


class School:
    def __init__(self, key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

schools = (
    School('hv',      'Happy Valley Elementary',   37.9045286, -122.1445772),
    School('stanley', 'Stanley Middle',            37.8884474, -122.1155922),
    School('wci',     'Walnut Creek Intermediate', 37.9093673, -122.0580063)
)
schools_by_key = {school.key: school for school in schools}


@app.route("/<school_code>")
def show_school(school_code):
    school = schools_by_key.get(school_code)
    if school:
        return render_template('map.html', school=school)
    else:
        abort(404)




if __name__ == '__main__':
   app.run(debug=True)