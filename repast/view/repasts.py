# coding: UTF-8
from flask import request, render_template
from repast.services.stores_service import *
from flask import request, render_template, redirect, url_for
from repast.services.queue_setting_service import *
from repast.services.stores_service import get_stores_by_id
from repast.services.shop_assistant import *
from repast.util.session_common import *


def to_repast_by_stores_id(stores_id):
    '''根据id到餐厅页面'''
    if stores_id == 1:
        message = '喵喵餐厅'
    if stores_id == 2:
        message = '饭饭餐厅'
    return render_template('repast.html',
                           stores_id=stores_id,
                           message=message)

def to_call_number():
    return render_template('reception/call_number.html')


def to_call_number(shop_assistant_id):
    '''员工登录成功后返回叫号页面'''
    set_session_user('shop_assistant_id', shop_assistant_id)
    stores_id = get_stores_id_by_shop_assistant_id(shop_assistant_id)
    stores_queue_info = get_now_queue_number_and_number_wait_by_stores_id(stores_id)
    stores = get_stores_by_id(stores_id)
    return render_template('reception/call_number.html',
                           stores_queue_info=stores_queue_info,
                           stores=stores)

def do_call_number(queue_id):
    '''叫号'''
    shop_assistant_id = get_session('shop_assistant_id')
    call_success = call_number(queue_id)
    return redirect(url_for('to_call_number', shop_assistant_id=shop_assistant_id))

def to_home():
    return render_template('reception/home.html')

def to_home_page(user_id):
    return render_template('reception/home_page.html',
                           nick_name=user_id)

def to_login():
    return render_template('reception/login.html')

def do_assistant_login():
    shop_assistant = get_shop_assistant_by_user(request)
    if shop_assistant:
        return redirect(url_for('to_call_number', shop_assistant_id=shop_assistant.id))
    else:
        return render_template('reception/login.html',
                               message='帐号或密码错误！')

def to_my_page():
    return render_template('reception/my_page.html')

def to_order_dishes():
    return render_template('reception/order_dishes.html')

def to_my_queue():
    return render_template('reception/queue.html')

def to_queue(stores_id):
    temp = get_queue_by_stores_id(stores_id)
    stores = get_stores_by_id(stores_id)
    return render_template('reception/reservation.html',
                           temp=temp,
                           stores=stores)

def do_queue():
    '''排队'''
    table_type_id = request.args.get('table_type_id') # 得到前端用户选择桌型
    queue = do_queue_format(table_type_id)
    return render_template('reception/reservation.html',
                           queue=queue)

def to_search():
    return render_template('reception/search.html')

def to_search_result():
    return render_template('reception/search_result.html')
