# coding: UTF-8
from flask import request, render_template
from repast.services.queue_setting_service import *
from repast.services.stores_service import get_stores_by_id


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

def to_home():
    return render_template('reception/home.html')

def to_home_page():
    nick_name = request.args.get('nickname')
    return render_template('reception/home_page.html',
                           nick_name=nick_name)

def to_login():
    return render_template('reception/login.html')

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

def to_search():
    return render_template('reception/search.html')

def to_search_result():
    return render_template('reception/search_result.html')
