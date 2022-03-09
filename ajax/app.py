from flask import Flask, render_template, jsonify
import numpy as np
app = Flask(__name__)

random_decimal=np.random.rand()
knk=1221
@app.route('/_get_current_user')
def get_current_user():
    global knk
    knk=knk+1
    x=str(knk)
    return x


@app.route('/')
def homepage():
    return render_template('home.html',x=random_decimal)


app.run(debug=True)