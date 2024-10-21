from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import pymysql
from pymysql.cursors import DictCursor

def connect_db(user_name: str, password: str):
    """
    MySQLとの接続を行う
    成功した場合はcheck_dbを呼び出し、
    dbに登録されているユーザとパスワードが一致するかを確認する
    失敗した場合はエラーを返す
    引数はブラウザに入力されたユーザ(username)、パスワード(password)である。
    """
    try:
        conn = mysql.connector.connect(
            host='db',  # Docker Composeでのサービス名を指定
            user='root',         #ログインする時のname
            password='YES',        #パスワード
            database='MyDatabase',#繋ぐdatebase
        )
            
        cur = conn.cursor()
        query = "SELECT user_name AS name, password FROM login WHERE user_name = %s"
        cur.execute(query, (user_name,))
        users = cur.fetchall()
        cur.close()
        conn.close()
        result = check_db(users, user_name, password)
        return result

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")
    

def check_db(users, user_name, password):
    """
    ユーザとパスワードが一致するかを判定する関数
    一致した場合はTrueをしなかった場合はFalseを返す
    引数はデータベースのユーザ情報とパスワード情報が入っている(user),
    ユーザによって入力された(username),パスワード(password)
    """                
    for user in users:
        if user_name == user[0] and password == user[1]:
            return True
    return False

def add_user(user_name: str, password: str, gender: str, birthday: str):
    """
    新規のユーザーとパスワードを追加し、ユーザー情報も user_infomation テーブルに登録する関数
    """
    try:
        conn = mysql.connector.connect(
            host='db',  # Docker Composeでのサービス名を指定
            user='root',# 本当のユーザに変更する
            password='YES', #本当のパスワードに変更する
            database='MyDatabase', # 本当のデータに変える
        )

        cur = conn.cursor()

        # login テーブルにユーザー名とパスワードを登録
        query_login = "INSERT INTO login (user_name, password) VALUES (%s, %s)"
        cur.execute(query_login, (user_name, password))
        user_id = cur.lastrowid  # 登録したユーザーの ID を取得

        # user_infomation テーブルに性別と年代を登録
        query_info = "INSERT INTO user_infomation (user_id, gendar, birthday) VALUES (%s, %s, %s)"
        cur.execute(query_info, (user_id, gender, birthday))

        conn.commit()
        cur.close()
        conn.close()

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")

def del_user(user_name: str, password: str):
    """
    MySQLとの接続を行い、ユーザーを削除する
    """
    try:
        conn = mysql.connector.connect(
            host='db',  # Docker Composeでのサービス名を指定
            user='root',
            password='YES',
            database='MyDatabase',
        )
            
        cur = conn.cursor()
        query = "DELETE FROM login WHERE user_name = %s"
        cur.execute(query, (user_name,))
        conn.commit()
        cur.close()
        conn.close()

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")
