import os


class DevelopmentConfig:

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4'.format(**{
        'user': os.getenv('DB_USER', 'hoge'),
        'password': os.getenv('DB_PASSWORD', 'huga'),
        'host': os.getenv('DB_HOST', '6188913504ff30da7b6ae47f720161f88bc0e85c7e9c7c1d6b70763bc6d75151'),
        'database': os.getenv('DB_DATABASE', 'app')
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig
