
from flask import Flask, render_template, request, jsonify, redirect
from backend.sqlite_conn import *
import copy
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return do_the_signup()

#    elif request.method == 'GET':
#        return get_user(id)
    else:
        return show_the_signup_form()

def show_the_signup_form():
	return render_template('prueba1.html')

def do_the_signup():
    error = None
    db = DBContext()
    result = db.add_user(request.form)
    db.conn.close()
    return redirect('/login')

@app.route('/test_vocacional', methods=['GET', 'POST'])
def test():
    return render_template('testvocacional.html')

@app.route('/main')
def main():
    return render_template('frontend/map.html')


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
    if valid_login(db, request.form):
        result = db.get_user(request.form)
        db.conn.close()
        #return str(result)
    else:
        return 'Invalid username/password'
    return redirect('/main')

def valid_login(db, form):
    result = db.get_user(form, ['user_name', 'password'])
    return True if result else False

def log_the_user_in(x):
    return jsonify(x)


    