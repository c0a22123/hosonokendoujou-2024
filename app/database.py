from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import pymysql
from pymysql.cursors import DictCursor
from flask import Flask
app = Flask(__name__)


def connect_db(username: str, password: str):
    """
    MySQLとの接続を行う
    成功した場合はcheck_dbを呼び出し、
    dbに登録されているユーザとパスワードが一致するかを確認する
    失敗した場合はエラーを返す
    引数はブラウザに入力されたユーザ(username)、パスワード(password)である。
    """
    try:
        conn = None 

        conn = mysql.connector.connect(
        host='db',  # Docker Composeでのサービス名を指定
        user='root',         #ログインする時のname
        password='YES',        #パスワード
        database='login_sample',#繋ぐdatebase
        )
            
        cur = conn.cursor()
        query = "SELECT user_name AS name, password FROM User WHERE user_name = %s"
        cur.execute(query, (username,))
        users = cur.fetchall()
        cur.close()
        conn.close()
        result = check_db(users, username, password)
        return result

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")
    
    

def check_db(users, username, password):
    """
    ユーザとパスワードが一致するかを判定する関数
    一致した場合はTrueをしなかった場合はFalseを返す
    引数はデータベースのユーザ情報とパスワード情報が入っている(user),
    ユーザによって入力された(username),パスワード(password)
    """                
    #if user and user['password'] == password:
    password_d = ""
    for user in users:
        if username == user[0]:
            password_d = user[1]
            if(password_d == password):
                return True
        else:
            return False

def add_user(username: str, password: str):
    """
    新規のユーザーとパスワードを追加するための関数
    ユーザによって入力された(username),パスワード(password)
    """ 
    try:
        conn = None 

        conn = mysql.connector.connect(
        host='db',  # Docker Composeでのサービス名を指定
        user='root',# 本当のユーザに変更する
        password='YES', #本当のパスワードに変更する
        database='login_sample', # 本当のデータに変える
        )

        cur = conn.cursor()
        query = "INSERT INTO User (user_name, password) VALUES (%s, %s)"
        cur.execute(query, (username, password))
        conn.commit()
        cur.close()
        conn.close()
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")  
    
def del_user(username: str, password: str):

    """
    MySQLとの接続を行う
    成功した場合はcheck_dbを呼び出し、
    dbに登録されているユーザとパスワードが一致するかを確認する
    失敗した場合はエラーを返す
    引数はブラウザに入力されたユーザ(username)、パスワード(password)である。
    """

    try:
        conn = None 
        conn = mysql.connector.connect(
        host='db',  # Docker Composeでのサービス名を指定
        user='root',
        password='YES',
        database='login_sample',
        )
            
        cur = conn.cursor()
        query = "DELETE FROM User WHERE user_name = %s"
        cur.execute(query,(username,))
        conn.commit()
        cur.close()
        conn.close()


    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")