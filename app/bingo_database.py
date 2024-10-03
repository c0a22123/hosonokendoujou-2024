from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import pymysql
from pymysql.cursors import DictCursor


def connect_db():
    conn = None 

    conn = mysql.connector.connect(
        host='db',  # Docker Composeでのサービス名を指定
        user='root',         #ログインする時のname
        password='YES',        #パスワード
        database='MyDatabase',#繋ぐdatebase
    )
    return  conn
def loadb_db(user_id: str):
    """
    MySQLとの接続を行う
    成功した場合はcheck_dbを呼び出し、
    dbに登録されているユーザとパスワードが一致するかを確認する
    失敗した場合はエラーを返す
    引数はブラウザに入力されたユーザ(username)、パスワード(password)である。
    """
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "SELECT * FROM bingo"
        cur.execute(query,)
        bingo = cur.fetchall()
        cur.close()
        conn.close()
        return bingo

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")

def update_bingo():
    conn = connect_db()
    cur = conn.cursor()
    query = f"""
    UPDATE {bingo}
    SET bingo_row0 = , bingo_row1 =%s, bingo_row2 =%s, bingo_row3 =%s, bingo_row4 =%s, bingo_row5 =%s, bingo_row6 =%S, bingo_row7 =%s, bingo_row8 =%s
    WHERE 
    """
    cur.execute(query,)
    conn.commit()
    bingo = cur.fetchall()
    cur.close()
    conn.close

def add_bingo(user_id: str, event_id: str,):
    """
    新規のユーザーとパスワードを追加するための関数
    ユーザによって入力された(username),パスワード(password)
    """ 
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "INSERT INTO bingo (user_id, event_id,bingo_row0,bingo_row1,bingo_row2,bingo_row3,bingo_row4,bingo_row5,bingo_row6,bingo_row7,bingo_row8, 0) VALUES (%s, %s,False, False,False,False, False,False,False, False,False,0)"
        cur.execute(query, (user_id, event_id))
        conn.commit()
        cur.close()
        conn.close()
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")  