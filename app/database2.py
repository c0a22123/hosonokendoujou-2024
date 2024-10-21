import mysql.connector

# データベース接続関数
def connect_db():
    connection = mysql.connector.connect(
        host="localhost",  # またはDockerコンテナ名
        user="root",       # ユーザー名
        password="your_password",  # パスワード
        database="MyDatabase"  # データベース名
    )
    return connection

# ユーザーの認証（ログイン処理）
def authenticate_user(username, password):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT user_id, password FROM login WHERE user_name = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user and user['password'] == password:  # ハッシュ化している場合はハッシュを使う
        return user['user_id']
    else:
        return None

# ユーザー情報の取得
def get_user_info(user_id):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT * FROM user_infomation WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    user_info = cursor.fetchone()

    cursor.close()
    conn.close()
    return user_info

# ビンゴ状態の取得
def get_bingo_status(user_id, event_id):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    
    query = """
        SELECT * FROM bingo 
        WHERE user_id = %s AND event_id = %s
    """
    cursor.execute(query, (user_id, event_id))
    bingo_status = cursor.fetchone()

    cursor.close()
    conn.close()
    return bingo_status

# ビンゴ状態の更新
def update_bingo(user_id, event_id, bingo_row, status):
    conn = connect_db()
    cursor = conn.cursor()
    
    query = f"UPDATE bingo SET {bingo_row} = %s WHERE user_id = %s AND event_id = %s"
    cursor.execute(query, (status, user_id, event_id))
    
    conn.commit()
    cursor.close()
    conn.close()

# 新しいユーザー登録
def add_new_user(username, password, gender, birthday):
    conn = connect_db()
    cursor = conn.cursor()

    # loginテーブルに挿入
    query = "INSERT INTO login (user_name, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    user_id = cursor.lastrowid

    # user_infomationテーブルに挿入
    query_info = "INSERT INTO user_infomation (user_id, gendar, birthday) VALUES (%s, %s, %s)"
    cursor.execute(query_info, (user_id, gender, birthday))

    conn.commit()
    cursor.close()
    conn.close()
