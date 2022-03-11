from flask import session, flash
import sys
sys.path.append("../")


from model.users import *
import datetime

def get_session_user():
    sessionuser=session.get('username', 'not set')
    sessionpassword=session.get('password','not set')
    return sessionuser,sessionpassword
    

def is_not_session_user():
    sessionuser=session.get('username', 'not set')
    sessionpassword=session.get('password','not set')
    if not sessionuser  =='not set' and not sessionpassword  =='not set':
        return True
    return False    


def is_have_session_user():
    sessionuser=session.get('username', 'not set')
    sessionpassword=session.get('password','not set')
    if (not sessionuser== 'not set' and not sessionpassword== 'not set') :
        return True
    return False
   

def getHourlyCarRequest(id,hour):
    doc=get_car_position_hourly(id,hour)
    hourr=hour
    total_minute_list=[]
    x_list=[]
    y_list=[]
    date_list=[]
    total_minute_list=[]
    
    for date, position in doc.items():
        minute = str(date[-2:]) 
        hour = str(date [-5:-3])
    
        if str(minute [0])==" ":
            minute=minute[1]
        if str(hour [0])==" ":
            hour=hour[1]
        
        total_min=  int(hour) * 60 +  int(minute)
        total_minute_list.append(total_min)

        x_list.append(position['x'])
        y_list.append(position['y'])
        date_list.append(date)
    total_minute_list,x_list,x_list,date_list=bubblesort(total_minute_list,x_list,x_list,date_list)
    total_minute_list =total_minute_list + total_minute_list
    x_list =x_list + x_list
    y_list =y_list + y_list
    date_list =date_list + date_list
    now = datetime.datetime.now()
    now_total_minute=now.hour*60 + now.minute
    maxminuteindex=total_minute_list.index(now_total_minute,1440)
    minminuteindex= maxminuteindex- int(hourr) * 60 

    x_list=x_list[minminuteindex:maxminuteindex]
    
    date_list=date_list[minminuteindex:maxminuteindex]
    y_list=y_list[minminuteindex:maxminuteindex]
    
    posts=[]
    
    x,y,date =   x_list , y_list,date_list
    for i in range(len(x)):
        post={
            'x':x[i],
            'y':y[i],
            'date':str(date[i])
        }
        posts.append(post)
        
    car={
        "id":id,
        "features":posts
    
    }
    return car 

def getAllCars_30_min_request():
    user_id=get_username_id(session.get('username'))
    car_id_list=getCarsIdFromUserId(user_id)
    cars=[]
    for car_id in car_id_list:
        car=get_30_min_request(car_id)
        cars.append(car)
    return cars
        
def get_30_min_request(id):
    
    now=datetime.datetime.now()
    current_minute=now.minute
    current_hour=now.hour
    x,y,date=get_car_for_last_30_min(id)

    
    posts=[]
        
    for j in range(31):
        
      
        
        for i in range(len(x)):
                      
            data_minute=int(date[i][-2:])
            data_hour=int(date[i][-5:-3])
            
            delta=now - datetime.timedelta(minutes=j)
           

            if data_minute ==delta.minute and data_hour ==delta.hour:
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
    print(len(car['features']))
    return car



def  add_user_request(username,email,password):
    add_user(username,email,password)




def is_avaiable_login(username,password):
    
    id= get_customer_id(username, password)
    if id != None:
        is_online(id,True)
        zaman=datetime.datetime.now()
        setLoginTime(id,zaman)
        resetFailedCount(id)
        session['username']=username
        session['password']=password

      
        return True 
    else:
       
        
            
        id= get_username_id(username)
        
        
        if int(updateFailedCount(id)) >=3:
            flash("3 kereden fazla hatalı giriş yaptınız. lütfen biraz daha dikkatli olalım.")
    
        return False


def user_logout():
    username=session['username']
    id= get_username_id(username)
    if 'username' in session:
        is_online(id,False)
        zaman=datetime.datetime.now()
        setLogoutTime(id, zaman)
        del session["username"]
        del session["password"]

        return True
    else:
        return False