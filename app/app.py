from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, Response,send_file, jsonify # type: ignore
import os
from pymysql.cursors import DictCursor
import qrcode
#import cv2 # type: ignore
from app.database import connect_db,add_user,del_user
import io
#from app.qrcode_utils import generate_qr, read_qr_from_camera

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# ビンゴシートの状態を保持するためのリスト
bingo_sheet = [False] * 9  # 3x3 ビンゴシート

# QRコード生成用関数
def generate_qr(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    return img

@app.route('/')
def index():
    #　usernameがセッションに登録されていれば、index.htmlへ　そうでなければ、login状態へ
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    #　入力されたusername、passwordがデータベースに登録されているのと一致したら、
    # sessionにusernameを登録し、index状態へ、そうでなければ、login.htmlへ
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result = connect_db(username, password) # 
        if(result):
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/add', methods=['GET', 'POST'])
#　passwordとpassword2が一致したら、usernameとpasswordをデータベースに登録する
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

@app.route('/bingo')
def bingo():
    return render_template('bingo.html')

@app.route('/generate_qr/<int:cell_id>')
def generate_qr_code(cell_id):
    # QRコードに埋め込むURLを設定
    url = str(cell_id)  # QRコードにはセルIDだけを埋め込む
    img = generate_qr(url)

    # QRコード画像をバイト形式で返す
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/stamp/<int:cell_id>')
def stamp(cell_id):
    # セルIDの範囲チェック
    if 1 <= cell_id <= 9:
        bingo_sheet[cell_id - 1] = True
        return jsonify(success=True, cell_id=cell_id)
    else:
        return jsonify(success=False)

if __name__ == '__main__':
    app.run(debug=True)