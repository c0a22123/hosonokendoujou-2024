# pythonのバージョンは任意
FROM python:3.9

WORKDIR /usr/src/app
ENV FLASK_APP=app

COPY /app/requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mysql-connector-python
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
