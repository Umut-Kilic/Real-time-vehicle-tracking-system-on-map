from flask import session, flash
import sys
sys.path.append("../")


from model.users import *
from datetime import datetime


def get_30_min_request(id):
    x,y,date=get_car_for_last_30_min(id)
    posts=[]
    for i in range(len(x)):
        post={
            'x':x[i],
            'y':y[i],
            'date':date[i]
        }
        posts.append(post)
    car={
        "id":id,
        "features":posts
    
    }
    pprint(car)
    return car

def  add_user_request(username,email,password):
    add_user(username,email,password)
    session['username']=username


def is_avaiable_login(username,password):
   
    id= get_customer_id(username, password)
    if id != None:
        is_online(id,True)
        zaman=datetime.now()
        setLoginTime(id,zaman)
        resetFailedCount(id)
        session['username']=username
        return True 
    else:
        id= get_username_id(username)
        if updateFailedCount(id) >=3:
            flash("Kardesim manyak mısın yalnıs girme artık ban yicen.")
    
        return False


def user_logout():
    username=session['username']
    id= get_username_id(username)
    if 'username' in session:
        is_online(id,False)
        zaman=datetime.now()
        setLogoutTime(id, zaman)
        del session["username"]
        return True
    else:
        return False