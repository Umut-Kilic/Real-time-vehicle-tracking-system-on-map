from flask import session, flash
import sys
sys.path.append("../")


from model.users import add_user , get_all_username,get_password,get_username_id,resetFailedCount,updateFailedCount,setLoginTime,setLogoutTime,get_customer_id,get_username_id
 
from datetime import datetime

def  add_user_request(username,email,password):
    add_user(username,email,password)
    session['username']=username


def is_avaiable_login(username,password):
    """if get_password(username) == password:
        session['username']=username
        return True 
    return False   """
    id= get_customer_id(username, password)
    #print("login id "+str(id))
    if id != None:
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
        zaman=datetime.now()
        setLogoutTime(id, zaman)
        del session["username"]
        return True
    else:
        return False

        
            


    

