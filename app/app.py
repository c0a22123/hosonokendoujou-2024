from flask import Flask, render_template, request, redirect, url_for, session, send_file, jsonify, flash
import qrcode
import io
from .database import *
from .bingodatabase import *
from .myfunction import *
from .spot_info import *
from .user_info import get_user_info

# ビンゴシートの状態を保持するためのリスト
bingo_sheet = [False] * 9

app = Flask(__name__, static_folder='./static')
app.secret_key = 'your_secret_key'
FILE_PNG_AB = 'qrcode_AB.png'

# セッション情報が保持されているか確認し、リクエストごとにユーザー情報を更新
@app.before_request
def load_user_info():
    user_id = session.get('user_id')
    if user_id:
        session['user_info'] = get_user_info(user_id)
    else:
        session['user_info'] = None

# コンテキストプロセッサを使って、すべてのテンプレートでログイン情報を利用可能に
@app.context_processor
def inject_user():
    return dict(logged_in=session.get('username') is not None, user_info=session.get('user_info'))

def bingo_check(bingo_list):
    ans = 0
    for i in range(2):
        if (bingo_list[i+2] == "True" and bingo_list[i+3] == "True" and bingo_list[i+4] == "True"):
            ans += 1
        if (bingo_list[i+2] == "True" and bingo_list[i+5] == "True" and bingo_list[i+8] == "True"):
            ans += 1
    if (bingo_list[2] == "True" and bingo_list[6] == "True" and bingo_list[10] == "True"):
        ans += 1
    if (bingo_list[4] == "True" and bingo_list[6] == "True" and bingo_list[8] == "True"):
        ans += 1
    return ans

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
    return render_template('index.html')

@app.route('/bingo')
def bingo():
    return render_template('bingo.html')

@app.route('/generate_qr/<int:cell_id>')
def generate_qr_code(cell_id):
    url = str(cell_id)
    img = generate_qr(url)

    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/stamp/<int:cell_id>')
def stamp(cell_id):
    try:
        if 1 <= cell_id <= 9:
            bingo_sheet[cell_id - 1] = True
            spot = spot_info.get(cell_id)
            if spot is None:
                raise ValueError(f"セルID {cell_id} に対応するスポット情報が見つかりません。")
            
            return jsonify(success=True, cell_id=cell_id, spot_name=spot["spot_name"], spot_trivia=spot["spot_trivia"])
        else:
            return jsonify(success=False, message="無効なセルIDです。")
    
    except Exception as e:
        print(f"サーバーエラー: {e}")
        return jsonify(success=False, message="サーバーでエラーが発生しました。"), 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = connect_db(username, password)
        
        if user:
            session['user_id'] = user['user_id']
            session['username'] = user['user_name']
            flash('ログインしました。', 'success')
            return redirect(url_for('index'))
        else:
            flash('ユーザー名またはパスワードが違います。', 'danger')
    
    return render_template('login.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        gender = request.form['gender']
        age = request.form['age']

        if password != password2:
            flash('パスワードが一致しません。', 'danger')
            return render_template('add.html')
        
        # パスワード重複チェック
        if is_password_duplicate(password):
            flash('そのパスワードはすでに使用されています。別のパスワードを選んでください。', 'danger')
            return render_template('add.html')
        
        # 新規ユーザーを追加
        add_user(username, password, gender, age)
        flash('ユーザーが追加されました。', 'success')
        return redirect(url_for('login'))
        
    return render_template('add.html')

        
    return render_template('add.html')

@app.route('/deleate', methods=['GET', 'POST'])
def deleate():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result = connect_db(username, password)
        if result:
            del_user(username, password)
            flash('ユーザーが削除されました。', 'success')
            return redirect(url_for('logout'))
    return render_template('deleate.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('ログアウトしました。', 'success')
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

@app.route('/humonji')
def humonji():
    return render_template('spot_info/humonji.html')

@app.route('/<sample_name>', methods=['GET', 'POST'])
def allpass(sample_name):
    global bingo_sheet 
    bingo_num = bingo_check(bingo_sheet)
    return render_template(f'{sample_name}.html', bingo_sheet=bingo_sheet, bingo_num=bingo_num)

@app.route('/waiting')
def waiting_page():
    return render_template('waiting.html')

@app.route('/sangyoumatsuri')
def sangyoumatsuri():
    return render_template('event/sangyo.html')

@app.route('/momiji')
def momiji():
    return render_template('event/momiji.html')

@app.route('/announce')
def announce():
    return render_template('announce.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# マイページのルートとユーザー情報の更新
@app.route('/mypage')
def mypage():
    user_info = session.get('user_info')
    return render_template('mypage.html', user_info=user_info)

@app.route('/user_change')
def user_change():
    user_info = session.get('user_info')
    if not user_info:
        flash('ログインしてください', 'danger')
        return redirect(url_for('login'))
    return render_template('user_change.html', user_info=user_info)


@app.route('/update_user_info', methods=['POST'])
def update_user_info():
    if not session.get('user_id'):
        flash('ログインしてください', 'danger')
        return redirect(url_for('login'))
    
    # フォームからのデータ取得
    new_username = request.form.get('username')
    new_gender = request.form.get('gender')
    new_birthday = request.form.get('birthday')

    # ユーザー情報の更新
    user_id = session['user_id']
    update_user_details(user_id, new_username, new_gender, new_birthday)

    # セッション情報の更新
    session['user_info'] = get_user_info(user_id)
    flash('ユーザー情報が更新されました', 'success')
    return redirect(url_for('mypage'))

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
