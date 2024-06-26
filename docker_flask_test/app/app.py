from flask import Flask, render_template, request, redirect, url_for, session
# from app.database import init_db,db
# from app.model import User
import mysql.connector
import pymysql
from pymysql.cursors import DictCursor
from app.database import connect_db, check_db

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result = connect_db(username, password)
        if(result):
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)


@app.route("/")
# def index():
#     return render_template("index.html")
def bingo():
    return render_template("bingo.html")
