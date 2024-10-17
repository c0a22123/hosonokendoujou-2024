from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import pymysql
from pymysql.cursors import DictCursor


def connectb_db():
    """
    データベースとの接続を行う
    これを使うことで毎回bingo_tableとの接続のためのコードを書かなくてよくなる
    引数は必要ないが、return がある為、conn=connect_db()のように利用する
    """
    conn = None 

    conn = mysql.connector.connect(
        host='db',  # Docker Composeでのサービス名を指定
        user='root',         #ログインする時のname
        password='YES',        #パスワード
        database='MyDatabase',#繋ぐdatebase
    )
    return  conn
def loadb_db(user_id: str, event_id: str):
    """
    MySQLとの接続を行う
    成功した場合はbingo_tableを呼び出し、
    dbに登録されている情報を確認する
    一般的にこの関数から参照してapp.pyを動かす
    """
    try:
        conn = connectb_db()
        cur = conn.cursor()
        query = "SELECT bingo_row0, bingo_row1,bingo_row2, bingo_row3, bingo_row4, bingo_row5, bingo_row6, bingo_row7, bingo_row8 FROM bingo WHERE user_id=%s AND event_id=%s"
        cur.execute(query,(user_id, event_id))
        bingo = cur.fetchall()
        cur.close()
        conn.close()
        return bingo

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")

def update_bingo(bingo_row:str , user_id:int, event_id:int):
    """
    データベースに登録されているビンゴを更新する
    引数として渡されたbingo_rowをTrueに変更する。列を特定するためにuser_idを使用する。
    """
    conn = connectb_db()
    cur = conn.cursor()
    query = "UPDATE bingo SET %s=True  where user_id = %s AND event_id=%s"
    cur.execute(query,(bingo_row, user_id, event_id))
    conn.commit()
    bingo = cur.fetchall()
    cur.close()
    conn.close

def add_bingo(user_id: str, event_id: str,):
    """
    ビンゴのデータベースの初期設定を行う。ユーザー登録をした際に、データベースに登録される。
    """ 
    try:
        conn = connectb_db()
        cur = conn.cursor()
        query = " INSERT INTO bingo (user_id, event_id,bingo_row0,bingo_row1,bingo_row2,bingo_row3,bingo_row4,bingo_row5,bingo_row6,bingo_row7,bingo_row8, total_bingo) VALUES (%s, %s, False, False,False, False, False, False, False, False, False, 0)"
        cur.execute(query, (user_id, event_id))
        conn.commit()
        cur.close()
        conn.close()
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました") 

def count_totalbingo(user_id:str, event_id: str,totalbingo):
    
    conn = connectb_db()
    cur = conn.cursor()
    query = "UPDATE bingo SET total_bingo=%s  where user_id = %s AND event_id=%s"
    cur.execute(query,(user_id, event_id, totalbingo))
    conn.commit()
    bingo = cur.fetchall()
    cur.close()
    conn.close

