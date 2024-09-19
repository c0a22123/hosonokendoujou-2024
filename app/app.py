from flask import Flask, render_template, request, redirect, url_for, session
# import cv2
# import pyqrcode
# from pymysql.cursors import DictCursor
from .database import connect_db, check_db,add_user,del_user



bingo_list=[[False,False,False],
            [False,False,False],
            [False,False,False]]

app = Flask(__name__, static_folder='./static')
app.secret_key = 'your_secret_key'
# font = cv2.FONT_HERSHEY_SIMPLEX
FILE_PNG_AB = 'qrcode_AB.png'

def bingo_check(bingo_list):
    '''
    引数：なし
    出力：ビンゴの数
    '''
    ans=0
    for i in range(3):
        if all(bingo_list[i]):
            ans+=1
            print(1)
        if all(row[i] for row in bingo_list):
            ans+=1
            print(2)
    if bingo_list[0][0] and bingo_list[1][1] and bingo_list[2][2]:
        ans+=1
        # print(3)
    if bingo_list[2][0] and bingo_list[1][1] and bingo_list[0][2]:
        ans+=1
        # print(3)
    return ans

@app.route('/')
def login_after():#ログイン済み確認
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
    return render_template('top')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']

        if(password == password2):
            add_user(username, password)
            return redirect(url_for('login'))
        
    return render_template('adduser.html')

@app.route('/deleate', methods=['GET', 'POST'])
def deleate():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result = connect_db(username, password)
        if(result):
            del_user(username,password)
            return redirect(url_for('logout'))
    return render_template('deleate.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


    

@app.route('/bingo_spot', methods=['GET','post'])
def index_3(num):
    global bingo_list
    num=int(num)
    bingo_list[int(num/3)][num%3]=True
    return render_template('bingo_spot.html')


@app.route('/<sample_name>', methods=['GET', 'POST'])
def allpass(sample_name):
    global bingo_list 
    bingo_num=bingo_check(bingo_list)
    return render_template(f'{sample_name}.html',bingo_list=bingo_list,bingo_num=bingo_num)

if __name__ == '__main__':
    app.run( debug=True)



