# coding: UTF-8


# flask模块需要的配置参数
# ===============================================================
DEBUG = True  # 是否启动调试功能
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT^&556gh/ghj~hj/kh'  # session相关的密匙

# models模块需要的配置参数
# ===============================================================
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/repast?charset=utf8'  # 连接的数据库

#SQLALCHEMY_DATABASE_URI = 'mysql://root:root@42.121.108.142:3306/repast?charset=utf8'  # 连接的数据库
SQLALCHEMY_ECHO = True  # 是否显示SQL语句

STORES_PICTURE_ALLOWED_EXTENSION = ('jpeg', 'png', 'jpg')
STORES_PICTURE_BASE_PATH = '/Users/K/Documents/Code/Python/repast_py/repast'
STORES_PICTURE_REL_PATH = '/static/images/stores'
# 基本的url
BASE_URL = "http://repast.kejukeji.com"
