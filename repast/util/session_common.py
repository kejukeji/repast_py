# coding: UTF-8
from flask import session


def get_session_user():
    if session.has_key('user') and session['user']:
        #这里只能传递一个字符串，不然会报没有序列化的错
        return session['user']
    return None

def get_session_shop_user():
    if session.has_key('shop_user') and session['shop_user']:
        #这里只能传递一个字符串，不然会报没有序列化的错
        return session['shop_user']
    return None

def set_session_user(key_name, value_name, key_id, value_id):
    """
       登陆成功保存到session当中
    """
    session[str(key_name)] = value_name
    session[str(key_id)] = value_id

