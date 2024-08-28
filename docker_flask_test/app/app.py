from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, Response, jsonify # type: ignore
import os
from pymysql.cursors import DictCursor
import qrcode
import cv2 # type: ignore
from app.database import connect_db,add_user,del_user
from app.qrcode_utils import generate_qr, read_qr_from_camera

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 事前に生成したQRコードデータ
qr_codes = [f'QR-{i+1}' for i in range(9)]

# ビンゴデータの初期化
bingo_data = [[None for _ in range(3)] for _ in range(3)]

# 'static'ディレクトリが存在しない場合は作成します
if not os.path.exists('static'):
    os.makedirs('static')

# 検出されたQRコードの状態を追跡
detected_qr_codes = set()

def generate_camera_stream():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        print("Frame grabbed")  # デバッグメッセージ

        data, bbox, _ = detector.detectAndDecode(frame)
        if bbox is not None:
            bbox = bbox.astype(int)  # 座標を整数に変換
            for i in range(len(bbox)):
                pt1 = tuple(bbox[i][0])
                pt2 = tuple(bbox[(i + 1) % len(bbox)][0])
                cv2.line(frame, pt1, pt2, color=(255, 0, 0), thickness=2)
            cv2.putText(frame, data, (bbox[0][0][0], bbox[0][0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            if data in qr_codes and data not in detected_qr_codes:
                index = qr_codes.index(data)
                row, col = divmod(index, 3)
                bingo_data[row][col] = data  # ビンゴデータを更新
                detected_qr_codes.add(data)
                print(f"Detected QR Code: {data}")

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()
    cv2.destroyAllWindows()
    print("Camera released")

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

@app.route('/scan_camera')
def scan_camera():
    return render_template('camera.html')

@app.route('/video_feed')
def video_feed():
    print("Video feed endpoint called")  # デバッグメッセージ
    return Response(generate_camera_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/bingo_data')
def get_bingo_data():
    return jsonify(bingo_data)

@app.route('/generate_qr')
def generate_qr_code():
    data = 'Example QR Code Data'
    file_name = 'static/qrcode.png'

    # 'static'ディレクトリが存在しない場合は作成します
    if not os.path.exists('static'):
        os.makedirs('static')

    generate_qr(data, file_name)
    return send_from_directory('static', 'qrcode.png')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)



if __name__ == '__main__':
    app.run(debug=True)


@app.route("/")
#def index():    
#    return render_template("index.html")
def bingo():
    return render_template("bingo.html")
