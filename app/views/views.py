from flask import Flask, redirect, url_for,render_template
app =Flask(__name__,template_folder='../templates',static_folder='../static')




#@app.route('/')
#def hello_admin():
#   return render_template("index.html")


@app.route('/')
def home():
   return render_template("index.html")

@app.route('/kayıtol')
def kayit_ol():
   return render_template("kayit.html")

@app.route('/icerik')
def icerik():
   return render_template("kayit.html")


if __name__ == '__main__':
   app.run()
