import os
from flask import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import request


# Firebase auth
cred = credentials.Certificate("./bi-tech-challenge-firebase-adminsdk-lb96n-c9e1358cc2.json")
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://bi-tech-challenge.firebaseio.com/'})
root = db.reference()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'safepasswordlol'


def get_auth(username, password):
    users = root.child('users').get()
    for (key,value) in users.items():
        if value["email"] == username and value["password"] == password:
            return value
    return None


def get_challenges():
    challenges = root.child('challenges').get()
    return challenges


def get_users():
    users = root.child('users').get()
    return users


def get_username(username):
    users = root.child('users').get()
    for (key,value) in users.items():
        if value["username"] == username:
            return value 
    return False


def get_usermail(mail):
    users = root.child('users').get()
    for (key,value) in users.items():
        if value["email"] == mail:
            return key,value 
    return False


def get_trains():
    trains = root.child('trains').get()
    return trains


def get_forum_questions():
    forum_questions = root.child('forum').get()
    return forum_questions


def get_question(question):
    forum_questions = get_forum_questions()
    for (key,value) in forum_questions.items():
        if value["title"] == question:
            return (key,value)
    return False


def answer_question(asked, author, answer):
    key,question = get_question(asked)
    to_push = {"author": author, "answer" : answer, "upvotes": 0}
    if question is not False:
        root.child('forum').child(key).child("answers").push(to_push)
        return True
    return False


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        auth = get_auth(request.form['username'], request.form['password'])
        if auth:
            return redirect('platform')
        else:
            return redirect('login')
    else:
        return render_template('auth.html')


@app.route('/platform',methods=['GET'])
def platform():
    users = get_users()
    wp_list = sorted(users.items(), key=lambda x: x[1]["wp"], reverse = True)
    fp_list = sorted(users.items(), key=lambda x: x[1]["fp"], reverse = True)
    hp_list = sorted(users.items(), key=lambda x: x[1]["hp"], reverse = True)
    return render_template('platform.html', wp_list = wp_list, fp_list = fp_list, hp_list = hp_list)


@app.route('/challenge', methods=['GET'])
def challenge():
    challenges = get_challenges()
    if challenges is None:
        challenges = {}
    return render_template('challenge.html', challenges = challenges)


@app.route('/challenge/add', methods=['GET','POST'])
def challenge_add():
    if request.method == 'POST':
        challenge = {"name": request.form["name"], "description": request.form["description"], "location": request.form["location"], "prize": request.form["prize"]}
        root.child("challenges").push(challenge)
        return redirect('challenge')
    else:
        return render_template('add_challenge.html')


@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    user = get_username(username)
    if user:
        return render_template('profile.html', user = user)
    else:
        return abort(404)


@app.route('/train', methods = ['GET'])
def train():
    trains = get_trains()
    return render_template('train.html',trains = trains)


@app.route('/forum', methods = ['GET'])
def forum():
    forum = get_forum_questions()
    return render_template('forum.html', forum = forum)


@app.route('/forum/add', methods = ['GET', 'POST'])
def create_question():
    if request.method == 'POST':
        # Add stuff
        print("oi")
    else:
        return render_template('add_question.html')

@app.route("/forum/show/<question>", methods=['GET','POST'])
def show_question(question):
    key,quest = get_question(question)
    if question is False:
        question = {}
    if request.method == 'POST':
        answer_question(question ,"Xico Santos", request.form["answer"])
    return render_template('show_question.html', question = quest) 

if __name__ == '__main__':
    app.run(debug=True)
