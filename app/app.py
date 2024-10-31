from flask import Flask, render_template, request, redirect, url_for, session, send_file, jsonify, flash
import qrcode
import io
from .database import *
from .bingodatabase import *
from .myfunction import *
from .spot_info import *
from .user_info import get_user_info
from datetime import datetime

# ビンゴシートの状態を保持するためのリスト


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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bingo')
def bingo():
    user_id = session.get('user_id')
    if not user_id:
        flash('ログインが必要です', 'danger')
        return redirect(url_for('login'))

    # ビンゴシートの状態を取得
    bingo_data = loadb_db(user_id, event_id="1")
    bingo_sheet = [str(row) == '1' for row in bingo_data[0]]

    # 景品交換状態を取得
    conn = connectb_db()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT exchanged FROM prize_exchange WHERE user_id = %s AND event_id = %s", (user_id, 1))
    prize_data = cur.fetchone()
    exchanged = prize_data['exchanged'] if prize_data else False  # データがなければ交換されていないと仮定
    cur.close()
    conn.close()

    return render_template('bingo.html', bingo_sheet=bingo_sheet, exchanged=exchanged)



@app.route('/stamp/<int:cell_id>')
def stamp(cell_id):
    try:
        user_id = session.get('user_id')
        event_id = 1  # イベントIDが1で固定の場合。動的に変更するならセッションから取得

        if user_id is None:
            return jsonify(success=False, message="ログインが必要です。")

        if 1 <= cell_id <= 9:
            # ビンゴシートの進捗をデータベースに記録
            update_bingo(f"bingo_row{cell_id - 1}", user_id, event_id)
            spot = spot_info.get(cell_id)
            if spot is None:
                raise ValueError(f"セルID {cell_id} に対応するスポット情報が見つかりません。")

            return jsonify(success=True, cell_id=cell_id, spot_name=spot["spot_name"], spot_trivia=spot["spot_trivia"])
        else:
            return jsonify(success=False, message="無効なセルIDです。")

    except Exception as e:
        print(f"サーバーエラー: {e}")
        return jsonify(success=False, message="サーバーでエラーが発生しました。"), 500
    
@app.route('/exchange_prize', methods=['POST'])
def exchange_prize():
    user_id = session.get('user_id')
    event_id = 1  # 例としてイベントIDを1に固定

    if not user_id:
        return jsonify(success=False, message="ログインが必要です。")

    conn = connectb_db()
    cur = conn.cursor(dictionary=True)

    # 景品交換の状態を確認
    cur.execute("SELECT exchanged FROM prize_exchange WHERE user_id = %s AND event_id = %s", (user_id, event_id))
    prize_data = cur.fetchone()

    # すでに交換済みの場合、メッセージを返す
    if prize_data and prize_data['exchanged']:
        return jsonify(success=False, message="景品は既に交換済みです。")
    
    # 新規または未交換の場合、交換状態を更新
    if prize_data:
        cur.execute("UPDATE prize_exchange SET exchanged = TRUE, exchange_date = %s WHERE user_id = %s AND event_id = %s",
                    (datetime.now(), user_id, event_id))
    else:
        cur.execute("INSERT INTO prize_exchange (user_id, event_id, exchanged, exchange_date) VALUES (%s, %s, TRUE, %s)",
                    (user_id, event_id, datetime.now()))
    
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(success=True, message="景品を交換しました。")

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

# 新規ユーザー登録後に bingo テーブルに初期データを追加
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
        
        if is_password_duplicate(password):
            flash('そのパスワードはすでに使用されています。別のパスワードを選んでください。', 'danger')
            return render_template('add.html')
        
        # 新規ユーザーを追加
        add_user(username, password, gender, age)
        
        # ユーザーID取得後に bingo テーブルに初期データを追加
        user_id = get_user_id(username)  # 新しく作成したユーザーの user_id を取得する関数
        if user_id:
            add_bingo(user_id, 1)  # event_id は仮に 1 を指定
            
            # 景品交換データをprize_exchangeテーブルに挿入
            conn = connectb_db()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO prize_exchange (user_id, event_id, exchanged) VALUES (%s, %s, %s)",
                (user_id, 1, False)  # event_idは仮に1を指定、交換済みをFalseで初期設定
            )
            conn.commit()
            cur.close()
            conn.close()

        flash('ユーザーが追加されました。', 'success')
        return redirect(url_for('login'))
    
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