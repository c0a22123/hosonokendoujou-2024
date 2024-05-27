# 簡単なindexページの作成を行っています。
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
# def index():
#     return render_template("index.html")
def bingo():
    return render_template("bingo.html")