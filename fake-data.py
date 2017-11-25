import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 

cred = credentials.Certificate("./bi-tech-challenge-firebase-adminsdk-lb96n-c9e1358cc2.json")
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://bi-tech-challenge.firebaseio.com/'})

root = db.reference()

archer = {"username": "Archer Sterling", "email": "archer@email.com", "country": "Portugal","section": "JavaDev", "team": "The Cereal Killers" ,"password" : "secret"} 
root.child("users").push(archer)
lana = {"username": "Lana Kane", "email": "lana@email.com", "country": "Portugal", "section": "PHPDev", "team": "The Cereal Killers", "password" : "secret"} 
root.child("users").push(lana)
malory = {"username": "Malory Sterling", "email": "malory@email.com", "country": "Portugal", "section": "PythonDev", "team": "The Cereal Killers", "password" : "secret"} 
root.child("users").push(malory)
rick = {"username": "Rick Sanchez", "email": "rick@email.com", "country": "Suiça", "section": "JavaDev", "team": "The Ricksters", "password" : "secret"} 
root.child("users").push(rick)
morty = {"username": "Morty Smith", "email": "morty@email.com", "country": "Suiça", "section": "PHPDev", "team": "The Ricksters", "password" : "secret"} 
root.child("users").push(morty)
mrpoopybuthole = {"username": "MrPoopyButhole", "email": "mrpoopybuthole@email.com", "country": "Suiça", "section": "PHPDev", "team": "The Ricksters", "password" : "secret"} 
root.child("users").push(mrpoopybuthole)
