from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import pymysql
from pymysql.cursors import DictCursor
import mysql.connector

def get_user_id(username):
    """
    新しく作成したユーザーの user_id を取得する関数
    """
    try:
        conn = mysql.connector.connect(
            host='db',
            user='root',
            password='YES',
            database='MyDatabase'
        )
        cursor = conn.cursor(dictionary=True)
        query = "SELECT user_id FROM login WHERE user_name = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user['user_id'] if user else None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def connectb_db():
    """
    データベースとの接続を行う関数。
    """
    conn = mysql.connector.connect(
        host='db',          # Docker Composeで指定したサービス名
        user='root',         # データベースのユーザー名
        password='YES',      # パスワード
        database='MyDatabase' # データベース名
    )
    return conn

def loadb_db(user_id: str, event_id: str):
    """
    指定されたユーザーIDとイベントIDに対応するビンゴデータを取得する関数。
    """
    try:
        conn = connectb_db()
        cur = conn.cursor()
        query = "SELECT bingo_row0, bingo_row1, bingo_row2, bingo_row3, bingo_row4, bingo_row5, bingo_row6, bingo_row7, bingo_row8 FROM bingo WHERE user_id=%s AND event_id=%s"
        cur.execute(query, (user_id, event_id))
        bingo = cur.fetchall()
        cur.close()
        conn.close()
        return bingo

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")

def update_bingo(bingo_row: str, user_id: int, event_id: int):
    """
    指定されたビンゴ行をチェック済みに更新する関数。
    """
    conn = connectb_db()
    cur = conn.cursor()
    query = f"UPDATE bingo SET {bingo_row} = True WHERE user_id = %s AND event_id = %s"
    cur.execute(query, (user_id, event_id))
    conn.commit()
    cur.close()
    conn.close()

def add_bingo(user_id: str, event_id: str):
    """
    ユーザーが新規登録した際に、ビンゴテーブルに初期データを追加する関数。
    """
    try:
        conn = connectb_db()
        cur = conn.cursor()
        query = """
            INSERT INTO bingo (user_id, event_id, bingo_row0, bingo_row1, bingo_row2, 
                               bingo_row3, bingo_row4, bingo_row5, bingo_row6, bingo_row7, 
                               bingo_row8, total_bingo) 
            VALUES (%s, %s, False, False, False, False, False, False, False, False, False, 0)
        """
        cur.execute(query, (user_id, event_id))
        conn.commit()
        cur.close()
        conn.close()

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")

def count_totalbingo(user_id: str, event_id: str, totalbingo: int):
    """
    ビンゴ数（ビンゴが達成された回数）を更新する関数。
    """
    conn = connectb_db()
    cur = conn.cursor()
    query = "UPDATE bingo SET total_bingo = %s WHERE user_id = %s AND event_id = %s"
    cur.execute(query, (totalbingo, user_id, event_id))
    conn.commit()
    cur.close()
    conn.close()

# ビンゴデータをセッションに保存
def load_bingo_data(user_id):
    session['bingo_data'] = loadb_db(user_id, 1)  # event_id は仮に 1 を指定
