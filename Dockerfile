# ベースイメージを指定
FROM python:3.8

# 作業ディレクトリを作成
WORKDIR /usr/src/app

# 依存関係のインストール
COPY app/requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
RUN pip install pymysql


# アプリケーションのソースコードをコピー
COPY app /usr/src/app

# ポートを指定
EXPOSE 5000

# Flaskコマンドはdocker-compose.ymlで指定されているため、CMDは不要です
