# coding: UTF-8
from flask import request, render_template
from repast.services.stores_service import *
from flask import request, render_template, redirect, url_for
from repast.services.queue_setting_service import *
from repast.services.stores_service import get_stores_by_id
from repast.services.shop_assistant import *
from repast.services.user_service import *
from repast.util.session_common import *
from ..services.call_number_service import PushMessage


def to_repast_by_stores_id(stores_id):
    '''根据id到餐厅页面'''
    if stores_id == 1:
        message = '喵喵餐厅'
    if stores_id == 2:
        message = '饭饭餐厅'
    return render_template('repast.html',
                           stores_id=stores_id,
                           message=message)


def to_call_number(shop_assistant_id):
    '''员工登录成功后返回叫号页面'''
    set_session_shop_user(shop_assistant_id)
    stores_id = get_stores_id_by_shop_assistant_id(shop_assistant_id)
    stores_queue_info = get_now_queue_number_and_number_wait_by_stores_id(stores_id)
    stores = get_stores_by_id(stores_id)
    return render_template('reception/call_number.html',
                           stores_queue_info=stores_queue_info,
                           stores=stores)

def do_call_number(queue_id):
    '''叫号'''
    shop_assistant_id = get_session_shop_user()
    push_message_service = PushMessage()
    push_message_service.push_message(queue_id)
    call_success = call_number(queue_id)
    return redirect(url_for('to_call_number', shop_assistant_id=shop_assistant_id))

def to_home():
    return render_template('reception/index.html')

def to_home_page():
    user_id = request.args.get('user_id')
    if user_id:
        set_session_user(user_id)
    mark_queue = request.args.get('mark_queue')
    set_session_mark_queue(mark_queue)
    return render_template('reception/index.html',
                           user_id=user_id)

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
    user_id = get_session_user()

    return render_template('reception/my_page.html')

def to_order_dishes():
    return render_template('reception/order_dishes.html')

def to_my_queue(user_id):
    set_session_user(user_id)
    user_schedule = get_schedule_by_user_id(user_id)
    stores = get_stores_by_id(user_schedule.stores_id)
    return render_template('reception/queue.html',
                           schedule=user_schedule,
                           stores=stores)

def to_queue(stores_id):
    user_id = request.args.get('user_id')
    if user_id:
        set_session_user(user_id)
    else:
        user_id = get_session_user()
    mark_queue = request.args.get('mark_queue')
    set_session_mark_queue(mark_queue) # 设置用户是否排队
    temp = get_queue_by_stores_id(stores_id)
    stores = get_stores_by_id(stores_id)
    return render_template('reception/reservation.html',
                           temp=temp,
                           stores=stores,
                           mark_queue=mark_queue)

def do_queue():
    '''排队'''
    user_id = get_session_user()
    table_type_id = request.args.get('table_type_id') # 得到前端用户选择桌型
    #user_id = int(request.args.get('user_id'))
    queue = do_queue_format(table_type_id, request, user_id)
    stores_id = queue.stores_id
    temp = get_queue_by_stores_id(stores_id)
    stores = get_stores_by_id(stores_id)
    return render_template('reception/reserv_success.html',
                           queue=queue,
                           message=queue.message,
                           temp=temp,
                           stores=stores)


def do_cancel_queue(queue_id):
    '''取消队列'''
    cancel(queue_id)
    stores_id = request.args.get('stores_id')
    my = request.args.get('my')
    if my:
        return redirect(url_for('to_my_line_up'))
    temp = get_queue_by_stores_id(stores_id)
    stores = get_stores_by_id(stores_id)
    mark_queue = 0
    return render_template('reception/reservation.html',
                           temp=temp,
                           stores=stores,
                           mark_queue=mark_queue)


def to_reservation():
    user_id = request.args.get('user_id')
    set_session_user(user_id)
    table_type_id = request.args.get('table_type_id')
    queue = do_queue_format(table_type_id, request, user_id)
    stores_id = request.args.get('stores_id')
    stores = get_stores_by_id(stores_id)
    return render_template('reception/reserv_success.html',
                           queue=queue,
                           stores=stores)

def to_search():
    user_id = get_session_user()
    mark_queue = get_session_mark_queue()
    if user_id:
        latitude = get_user_by_id(user_id).latitude
        longitude = get_user_by_id(user_id).longitude
        des = get_user_by_id(user_id).description
        if des:
            description = des[:-12]
        else:
            description = ''
        if latitude and longitude:
            return render_template('reception/search.html',
                                   latitude=latitude,
                                   longitude=longitude,
                                   description=description,
                                   mark_queue=mark_queue,
                                   user_id=user_id)
        else:
            return render_template('reception/search_copy.html',
                                   mark_queue=mark_queue,
                                   user_id=user_id)
    else:
        return render_template('reception/search_copy.html',
                               mark_queue=mark_queue,
                               user_id=user_id)

def to_search_position():
    user_id = get_session_user()
    mark_queue = get_session_mark_queue()
    return render_template('reception/search_copy.html',
                           mark_queue=mark_queue,
                           user_id=user_id)

def to_search_result():
    user_id = get_session_user()
    mark_queue = get_session_mark_queue()
    return render_template('reception/search_result.html',
                           mark_queue=mark_queue,
                           user_id=user_id)


def to_my_line_up():
    user_id = request.args.get('user_id')
    if user_id is None:
        user_id = get_session_user()
    else:
        set_session_user(user_id)
    my_line_up_info = get_schedule_by_user_id(user_id)
    return render_template('reception/my_line_up.html',
                           my_line_up_info=my_line_up_info)
