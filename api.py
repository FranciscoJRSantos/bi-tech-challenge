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


@app.route('/')
def hello():
    return 'Hello World!'


def get_auth(username,password):
    users = root.get('users')
    if username in users:
        return users.get(username)
    return None

def get_challenges():
    challenges = root.child('challenges').get()
    return challenges

def get_users():
    users = root.child('users').get()
    return users

def get_sections():
    sections = root.child('sections').get()
    return sections

def get_teams():
    teams = root.child('teams').get()
    return teams

def get_countries():
    countries = root.child('countries').get()
    return countries


@app.route('/auth', methods=['GET','POST'])
def auth():
    if request.method == 'POST':
        auth = get_auth(request.form['username'],request.form['password'])
        return render_template('home.html') if auth else redirect('plat')
    else:
        return render_template('auth.html')


@app.route('/plat',methods=['GET'])
def plaf():
    users = get_users()
    users_list = sorted(users.items(), key=lambda x: x[1]["points"], reverse = True)
    teams = get_teams()
    teams_list = sorted(teams.items(), key=lambda x: x[1]["points"], reverse = True)
    sections = get_sections()
    sections_list = sorted(sections.items(), key=lambda x: x[1]["points"], reverse = True)
    countries = get_countries()
    countries_list = sorted(countries.items(), key=lambda x: x[1]["points"], reverse = True)
    return render_template('login.html', users_list = users_list, teams_list = teams_list, sections_list = sections_list, countries_list = countries_list)


@app.route('/challenge', methods=['GET'])
def challenge():
    challenges = get_challenges()
    return render_template('challenge.html', challenges = challenges)


@app.route('/challenge/add', methods=['GET','POST'])
def challenge_add():
    if request.method == 'POST':
        challenge = {"name": request.form["name"], "description": request.form["description"], "location": request.form["location"], "prize": request.form["prize"]}
        root.child("challenges").push(challenge)
        return redirect('challenge')
    else:
        return render_template('add_challenge.html')


if __name__ == '__main__':
    app.run()
