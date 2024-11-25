from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import pymysql
from pymysql.cursors import DictCursor

def connect_db(user_name: str, password: str):
    """
    MySQLとの接続を行い、ユーザー情報を取得する。
    成功した場合はユーザーIDとユーザー名を返し、パスワードが一致しない場合はNoneを返す。
    """
    try:
        conn = mysql.connector.connect(
            host='db',  # Docker Composeでのサービス名を指定
            user='root',
            password='YES',
            database='MyDatabase'
        )
            
        cur = conn.cursor(dictionary=True)
        query = "SELECT user_id, user_name, password FROM login WHERE user_name = %s"
        cur.execute(query, (user_name,))
        user = cur.fetchone()

        if user and user['password'] == password:
            return {'user_id': user['user_id'], 'user_name': user['user_name']}
        else:
            return None

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")

    finally:
        cur.close()
        conn.close()

def check_db(users, user_name, password):
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
            host='db',
            user='root',
            password='YES',
            database='MyDatabase',
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

        return user_id  # 新しく追加したユーザーIDを返す

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")

def del_user(user_name: str, password: str):
    """
    MySQLとの接続を行い、ユーザーと関連する情報を削除する
    """
    try:
        conn = mysql.connector.connect(
            host='db',
            user='root',
            password='YES',
            database='MyDatabase',
        )
        
        cur = conn.cursor()

        # ユーザーIDを取得
        query = "SELECT user_id FROM login WHERE user_name = %s AND password = %s"
        cur.execute(query, (user_name, password))
        result = cur.fetchone()
        
        if result:
            user_id = result[0]
            
            # 1. `user_infomation` テーブルから先に削除
            query = "DELETE FROM user_infomation WHERE user_id = %s"
            cur.execute(query, (user_id,))

            # 2. 次に `login` テーブルからユーザーを削除
            query = "DELETE FROM login WHERE user_id = %s"
            cur.execute(query, (user_id,))

            conn.commit()
        
        cur.close()
        conn.close()

    except mysql.connector.Error as e:
        print(f"Error deleting user: {e}")
        raise Exception("ユーザーの削除に失敗しました")


def get_user_info(user_id):
    """
    指定されたユーザーIDに基づいてユーザー情報を取得する関数。
    """
    try:
        conn = mysql.connector.connect(
            host='db',
            user='root',
            password='YES',
            database='MyDatabase'
        )
        cursor = conn.cursor(dictionary=True)
        
        query = """
        SELECT login.user_name, user_infomation.gendar, user_infomation.birthday 
        FROM login 
        JOIN user_infomation ON login.user_id = user_infomation.user_id 
        WHERE login.user_id = %s
        """
        
        cursor.execute(query, (user_id,))
        user_info = cursor.fetchone()
        cursor.close()
        conn.close()
        
        return user_info

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")

def update_user_info(user_id, username, gender, age):
    """
    ユーザー情報を更新する関数。
    """
    try:
        conn = mysql.connector.connect(
            host='db',
            user='root',
            password='YES',
            database='MyDatabase'
        )
        cursor = conn.cursor()
        
        query_login = "UPDATE login SET user_name = %s WHERE user_id = %s"
        query_info = "UPDATE user_infomation SET gendar = %s, birthday = %s WHERE user_id = %s"
        
        cursor.execute(query_login, (username, user_id))
        cursor.execute(query_info, (gender, age, user_id))
        
        conn.commit()
        cursor.close()
        conn.close()
        return True

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")

def delete_user_account(user_id):
    """
    指定されたユーザーIDに基づいてユーザーアカウントを削除する関数。
    """
    try:
        conn = mysql.connector.connect(
            host='db',
            user='root',
            password='YES',
            database='MyDatabase'
        )
        cursor = conn.cursor()
        
        query_login = "DELETE FROM login WHERE user_id = %s"
        query_info = "DELETE FROM user_infomation WHERE user_id = %s"
        
        cursor.execute(query_info, (user_id,))
        cursor.execute(query_login, (user_id,))
        
        conn.commit()
        cursor.close()
        conn.close()
        return True

    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        raise Exception("MySQLサーバへの接続に失敗しました")

# ユーザー情報の更新用関数（database.py に記述）
def update_user_details(user_id, new_username, new_gender, new_birthday):
    """
    ユーザー情報を更新する関数
    """
    try:
        conn = mysql.connector.connect(
            host='db',
            user='root',
            password='YES',
            database='MyDatabase'
        )
        cur = conn.cursor()

        query = """
        UPDATE login 
        SET user_name = %s 
        WHERE user_id = %s
        """
        cur.execute(query, (new_username, user_id))

        query = """
        UPDATE user_infomation 
        SET gendar = %s, birthday = %s 
        WHERE user_id = %s
        """
        cur.execute(query, (new_gender, new_birthday, user_id))

        cur.close()  # ここでカーソルを閉じる
        conn.commit()  # カーソルが閉じられた後にコミット

    except mysql.connector.Error as e:
        print(f"Error updating user details: {e}")
        raise Exception("ユーザー情報の更新に失敗しました")

    finally:
        conn.close()  # 接続を閉じる
        
def is_password_duplicate(password):
    """
    データベース内でパスワードが重複しているか確認する関数
    重複があればTrue、なければFalseを返す
    """
    try:
        conn = mysql.connector.connect(
            host='db',
            user='root',
            password='YES',
            database='MyDatabase',
        )
        cur = conn.cursor()
        query = "SELECT COUNT(*) FROM login WHERE password = %s"
        cur.execute(query, (password,))
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result[0] > 0  # 重複があればTrue
    except mysql.connector.Error as e:
        print(f"Error checking password duplication: {e}")
        return False