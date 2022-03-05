import firebase_admin 
from firebase_admin import credentials ,firestore

kimlik= credentials.Certificate('./key.json')
app=firebase_admin.initialize_app(kimlik)
db=firestore.client()
document=db.collection("data").document("veri1")

document.set({
    
"veriyazi":"x"
})