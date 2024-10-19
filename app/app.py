from flask import Flask, render_template, request, redirect, url_for, session, send_file, jsonify
import qrcode
import io
from .database import *
from .bingo_database import *
from .myfunction import *


# ビンゴシートの状態を保持するためのリスト
bingo_sheet = loadb_db("1", "1") # 3x3 ビンゴシート


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
    for i in range(2):
        if (bingo_list[i+2] == "True" and bingo_list[i+3] == "True",bingo_list[i+4] == "True"):
            ans+=1
        if (bingo_list[i+2] == "True" and bingo_list[i+5] == "True" and bingo_list[i+8] == "True"):
            ans+=1
    if (bingo_list[i+2] == "True" and bingo_list[i+6] == "True" and bingo_list[i+10] == "True"):
        ans+=1
    if (bingo_list[i+4] == "True" and bingo_list[i+6] == "True" and bingo_list[i+8] == "True"):
        ans+=1
        # print(3)
    return ans

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

@app.route('/index')
def index():#ログイン済み確認
    return render_template('index.html')
    #return redirect(url_for('login'))

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = connect_db(username, password)
        if(result):
            session['username'] = username
            return redirect(url_for('index'))
            #return render_template('top.html')
    return render_template('login.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']

        if(password == password2):
            add_user(username, password)
            return redirect(url_for('login'))
        
    return render_template('add.html')

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


@app.route('/spot')
def route():
    return render_template('spot.html')

@app.route('/honzin')
def honzin():
    return render_template('spot_info/honzin.html')

@app.route('/housen')
def housen():
    return render_template('spot_info/housen.html')

@app.route('/hurusato')
def hurusato():
    return render_template('spot_info/hurusato.html')

@app.route('/kouryuu')
def kouryuu():
    return render_template('spot_info/kouryuu.html')

@app.route('/satou')
def satou():
    return render_template('spot_info/satou.html')

@app.route('/taisyou')
def taisyou():
    return render_template('spot_info/taisyou.html')

@app.route('/yasaka')
def yasaka():
    return render_template('spot_info/yasaka.html')

@app.route('/zizou')
def zizou():
    return render_template('spot_info/zizou.html')



@app.route('/<sample_name>', methods=['GET', 'POST'])
def allpass(sample_name):
    global bingo_sheet 
    bingo_num=bingo_check(bingo_sheet)
    return render_template(f'{sample_name}.html',bingo_sheet=bingo_sheet,bingo_num=bingo_num)

@app.route('/waiting')
def waiting_page():
    return render_template('waiting.html')
if __name__ == '__main__':
    app.run(debug=True)



