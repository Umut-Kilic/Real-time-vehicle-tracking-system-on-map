from flask import session
import sys
sys.path.append("../")


from model.users import add_user , get_all_username,get_password
 


def  add_user_request(username,email,password):
    add_user(username,email,password)
    session['username']=username


def is_avaiable_login(username,password):
    if get_password(username) == password:
        session['username']=username
        return True 
    return False       

def user_logout():
    if "username" in session:
        del session["username"]
        return True
    else:
        return False

        
            


    

