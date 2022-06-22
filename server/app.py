from flask import Flask, render_template, request, session, redirect
from flask_session import Session
import sqlite3 as sql

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def main():
    return render_template('reg.html')


@app.route('/register_confirmation', methods=['GET', 'POST'])
def registered():
    name = request.form.get('uname')
    pass_w = request.form.get('pass')

    with sql.connect('database.db') as db:
        db.execute("INSERT INTO users (u_name, pass) VALUES(?, ?)", (name, pass_w))

    return render_template('register_success.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        name = request.form.get('uname')
        pass_w = request.form.get('pass')

        with sql.connect('database.db') as db:
            pass_check = db.execute("SELECT pass FROM users WHERE u_name = (?)", (name,))
        
        for i in pass_check:
            for j in i:
                if j == pass_w:
                    session['name'] = name
                    return redirect('/create')
                else:
                    return render_template('error.html')
    else:
        return render_template('CreateUrl.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/list', methods=['GET', 'POST'])
def listing():
    name = session.get('name')

    if request.method == 'POST':
        o_url = request.form.get('o_url')
        n_url = request.form.get('n_url')
        print(o_url)
        print(n_url)
        print(name)

        with sql.connect('database.db') as db:
            db.execute('UPDATE users SET o_url = ?, n_url = ? WHERE u_name= ?', (o_url, n_url, name))
        return redirect('/list')

    else:
        with sql.connect('database.db') as db:
            urls = db.execute('SELECT n_url, o_url FROM USERS WHERE u_name = (?)', (name,))
        return render_template('listing.html', urls=urls, name=name)
