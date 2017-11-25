import os
from flask import *
from flask_httpauth import HTTPDigestAuth
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from trello import TrelloApi
from flask import request

# Firebase auth
cred = credentials.Certificate("./bi-tech-challenge-firebase-adminsdk-lb96n-c9e1358cc2.json")
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://bi-tech-challenge.firebaseio.com/'})
root = db.reference()

# Trello Auth
trello = TrelloApi(os.environ.get('TRELLO_KEY'))
trello.boards.get('4d5ea62fd76aa1136000000c')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'safepasswordlol'
auth = HTTPDigestAuth()

@app.route("/")
def hello():
    return "Hello World!"

def get_auth(username,password):
    # Query firebase || Leave this for now
    users = root.get("users")
    if username in users:
        return users.get(username)
    return None

@app.route("/auth", methods=['GET','POST'])
def auth():
    if request.method == 'POST':
        auth = get_auth(request.form['username'],request.form['password'])
        return render_template('home.html') if auth else redirect('plat')
    else:
        return render_template('auth.html')


@app.route("/plat",methods=['GET'])
def plaf():
    return render_template('login.html')
if __name__ == '__main__':
    app.run()
