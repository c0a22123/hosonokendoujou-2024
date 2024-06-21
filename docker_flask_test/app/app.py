from flask import Flask, render_template, request, redirect, url_for, session
from app.database import init_db,db
from app.model import User

app = Flask(__name__)
app.secret_key = 'your_secret_key'

<<<<<<< HEAD
# ダミーのユーザーデータベース
users = {'admin': 'password'}

@app.route('/')
def index():
    if 'username' in session:
        print("a")
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Invalid username/password'

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/show')
def show_users():
    all_peter = User.query.filter_by(name='peter').all()
    how_many_peter = len(all_peter)
    return '今Peterは{}人います'.format(how_many_peter)

@app.route('/add')
def add_user():
    peter = User(name='peter')
    db.session.add(peter)
    db.session.commit()
    return 'Peterを増やしました。'

@app.route('/delete')
def delete_user():
    peter = User.query.filter_by(name='peter').first()
    if peter is not None:
        db.session.delete(peter)
        db.session.commit()
        return 'Peterを減らしました。'
    else:
        return 'Peterはひとりもいません'

if __name__ == '__main__':
    app.run(debug=True)


=======
@app.route("/")
# def index():
#     return render_template("index.html")
def bingo():
    return render_template("bingo.html")
>>>>>>> bd0dec5e7331eb0af0f09edcbaed1c83e441b341
