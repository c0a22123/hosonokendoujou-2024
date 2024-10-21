from flask import Flask, render_template, session
import mysql.connector

def get_user_info(user_id):
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='YES',
        database='MyDatabase'
    )
    cursor = conn.cursor(dictionary=True)
    
    # SQLクエリでloginテーブルとuser_infomationテーブルをJOINして情報を取得
    query = """
    SELECT login.user_name, user_infomation.gendar, user_infomation.birthday 
    FROM login 
    JOIN user_infomation ON login.user_id = user_infomation.user_id 
    WHERE login.user_id = %s
    """
    
    cursor.execute(query, (user_id,))
    user_info = cursor.fetchone()  # ユーザー情報を1件取得
    cursor.close()
    conn.close()
    
    return user_info