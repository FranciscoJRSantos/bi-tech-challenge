import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 

cred = credentials.Certificate("./bi-tech-challenge-firebase-adminsdk-lb96n-c9e1358cc2.json")
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://bi-tech-challenge.firebaseio.com/'})

root = db.reference()

archer = {"name": "Sterling Archer", "agency": "Figgis Agency", "password" : "secret101"} 
root.child("users").push(archer)
lana = {"name": "Lana Kane", "agency": "Figgis Agency", "password" : "safepasswordlol"} 
root.child("users").push(lana)
