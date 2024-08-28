# pythonのバージョンは任意
FROM python:3.9

WORKDIR /usr/src/app
ENV FLASK_APP=app

COPY /app/requirements.txt ./

RUN apt-get update
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install mysql-connector-python
RUN pip install pymysql
RUN pip install opencv-python
RUN pip install opencv-contrib-python
RUN apt-get install -y libgl1-mesa-dev
RUN pip install qrcode[pil] opencv-python-headless
RUN pip install Pillow
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
