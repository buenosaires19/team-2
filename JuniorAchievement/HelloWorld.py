
from flask import Flask, render_template, request, jsonify
from backend.sqlite_conn import *

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/pepe")
def pepe():
	return "Hola pepe"


@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
#    elif request.method == 'GET':
#        return get_user(id)
    else:
        return show_the_login_form()

def show_the_login_form():
	return render_template('login.html')

def do_the_login():
    error = None
    db = DBContext()
    if request.method == 'POST':
        if valid_login(db, request.form):
            result = db.get_user(request.form, ['user_name', 'password'])
            return str(result)
        else:
            return 'Invalid username/password'

    return render_template('login.html', error=error)

def valid_login(db, form):
    result = db.get_user(form, ['user_name', 'password'])
    return True if result else False

def log_the_user_in(x):
    return jsonify(x)


    