import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 

cred = credentials.Certificate("./bi-tech-challenge-firebase-adminsdk-lb96n-c9e1358cc2.json")
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://bi-tech-challenge.firebaseio.com/'})

root = db.reference()

archer = {"username": "ArcherSterling", "email": "archer@email.com", "country": "Portugal","section": "JavaDev", "password" : "secret", "wp": 5, "hp" : 5, "fp" : 50 } 
root.child("users").push(archer)
lana = {"username": "LanaKane", "email": "lana@email.com", "country": "Portugal", "section": "PHPDev", "password" : "secret","wp": 15, "hp" : 5, "fp" : 50} 
root.child("users").push(lana)
malory = {"username": "MalorySterling", "email": "malory@email.com", "country": "Portugal", "section": "PythonDev", "password" : "secret","wp": 7, "hp" : 5, "fp" : 50} 
root.child("users").push(malory)
rick = {"username": "RickSanchez", "email": "rick@email.com", "country": "Suiça", "section": "JavaDev", "password" : "secret", "wp": 6, "hp": 5, "fp": 50} 
root.child("users").push(rick)
morty = {"username": "MortySmith", "email": "morty@email.com", "country": "Suiça", "section": "PHPDev", "password" : "secret", "wp": 10 , "hp" : 5, "fp" : 50} 
root.child("users").push(morty)
mrpoopybuthole = {"username": "MrPoopyButhole", "email": "mrpoopybuthole@email.com", "country": "Suiça", "section": "PythonDev", "password" : "secret", "wp": 9, "hp" : 5, "fp" : 50} 
root.child("users").push(mrpoopybuthole)

lunch_train = {"name": "Almoço", "location": "4ºPiso","location" : "4ºPiso", "users": {1: "ArcherSterling", 2: "LanaKane"}}
root.child("trains").push(lunch_train)
rick_train = {"name":"wubalubadubdub coffee", "location": "Na dimensão C137, nos escritorios da BI, 8º Piso", "data": "25 Novembro 2017 - 17:30" ,"users": {1: "RickSanchez", 2: "MortySmith"}}
root.child("trains").push(rick_train)

forum_question1 = {"title": "Why should I work in PHP", "author": "RickSanchez", "section" : "PHPDev","answers": {1: {"author": "ArcherSterling", "answer": "You shouldn't, its bad >:/"}, 2: {"author": "MortySmith", "answer": "Well it actually depends on the project you're working on, and your experience with the language, but overall it's a preety good scripting language"}}}
root.child("forum").push(forum_question1)
