import mysql.connector
import pymysql

def connectb_db():
    """
    データベースとの接続を行う
    """
    conn = mysql.connector.connect(
        host='db',  # Docker Composeでのサービス名を指定
        user='root',         # ログインする時のユーザー名
        password='YES',      # パスワード
        database='MyDatabase',  # 接続するデータベース
    )
    return conn

def loadb_db(user_id: str, event_id: str):
    """
    MySQLからビンゴシートの情報を取得して、ビンゴ状態を返す
    """
    try:
        conn = connectb_db()
        cur = conn.cursor()
        query = """
            SELECT 
                bingo_row0, bingo_row1, bingo_row2, 
                bingo_row3, bingo_row4, bingo_row5, 
                bingo_row6, bingo_row7, bingo_row8 
            FROM bingo 
            WHERE user_id=%s AND event_id=%s
        """
        cur.execute(query, (user_id, event_id))
        result = cur.fetchone()
        cur.close()
        conn.close()

        # ビンゴシートの行をリスト形式に変換して返す
        if result:
            return list(result)
        else:
            return [False] * 9  # デフォルトでは全て未チェック
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")

def update_bingo(bingo_row:str , user_id:int, event_id:int):
    """
    データベースに登録されているビンゴの特定の行（bingo_row）をTrueに変更する
    """
    try:
        conn = connectb_db()
        cur = conn.cursor()

        # 特定の列を更新するクエリを構築
        query = f"UPDATE bingo SET {bingo_row}=True WHERE user_id = %s AND event_id=%s"
        cur.execute(query, (user_id, event_id))
        conn.commit()
        cur.close()
        conn.close()
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("ビンゴの状態更新に失敗しました")

def add_bingo(user_id: str, event_id: str):
    """
    ユーザー登録時に新しいビンゴシートをデータベースに追加
    """
    try:
        conn = connectb_db()
        cur = conn.cursor()
        query = """
        INSERT INTO bingo (
            user_id, event_id, 
            bingo_row0, bingo_row1, bingo_row2, 
            bingo_row3, bingo_row4, bingo_row5, 
            bingo_row6, bingo_row7, bingo_row8, 
            total_bingo
        ) 
        VALUES (%s, %s, False, False, False, False, False, False, False, False, False, 0)
        """
        cur.execute(query, (user_id, event_id))
        conn.commit()
        cur.close()
        conn.close()
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("ビンゴシートの初期化に失敗しました")

def count_totalbingo(user_id: str, event_id: str, totalbingo: int):
    """
    データベース内のtotal_bingoを更新
    """
    try:
        conn = connectb_db()
        cur = conn.cursor()
        query = "UPDATE bingo SET total_bingo=%s WHERE user_id = %s AND event_id=%s"
        cur.execute(query, (totalbingo, user_id, event_id))
        conn.commit()
        cur.close()
        conn.close()
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("トータルビンゴのカウント更新に失敗しました")
