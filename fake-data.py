import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 

cred = credentials.Certificate("./bi-tech-challenge-firebase-adminsdk-lb96n-c9e1358cc2.json")
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://bi-tech-challenge.firebaseio.com/'})

root = db.reference()

archer = {"username": "ArcherSterling", "email": "archer@email.com", "country": "Portugal","section": "JavaDev", "team": "The Cereal Killers" ,"password" : "secret", "points": 5} 
root.child("users").push(archer)
lana = {"username": "LanaKane", "email": "lana@email.com", "country": "Portugal", "section": "PHPDev", "team": "The Cereal Killers", "password" : "secret","points": 15} 
root.child("users").push(lana)
malory = {"username": "MalorySterling", "email": "malory@email.com", "country": "Portugal", "section": "PythonDev", "team": "The Cereal Killers", "password" : "secret","points": 7} 
root.child("users").push(malory)
rick = {"username": "RickSanchez", "email": "rick@email.com", "country": "Suiça", "section": "JavaDev", "team": "The Ricksters", "password" : "secret", "points": 6} 
root.child("users").push(rick)
morty = {"username": "MortySmith", "email": "morty@email.com", "country": "Suiça", "section": "PHPDev", "team": "The Ricksters", "password" : "secret", "points": 10 } 
root.child("users").push(morty)
mrpoopybuthole = {"username": "MrPoopyButhole", "email": "mrpoopybuthole@email.com", "country": "Suiça", "section": "PythonDev", "team": "The Ricksters", "password" : "secret", "points": 9} 
root.child("users").push(mrpoopybuthole)

TCK = {"name": "The Cereal Killers", "points": 27, "country": "Portugal" }
root.child("teams").push(TCK)
TR = {"name": "The Ricksters", "points": 25, "country": "Suiça" }
root.child("teams").push(TR)

PythonDev = {"name": "PythonDev", "points": 16}
root.child("sections").push(PythonDev)
PHPDev = {"name": "PHPDev", "points": 25 }
root.child("sections").push(PHPDev)
JavaDev = {"name": "JavaDev", "points": 11}
root.child("sections").push(JavaDev)

Portugal = {"name": "Portugal", "points": 27}
root.child("countries").push(Portugal)
Suica = {"name": "Suiça", "points": 25 }
root.child("countries").push(Suica)
