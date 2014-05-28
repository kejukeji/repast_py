#! /usr/bin/python
# coding: utf-8
from flask import render_template, request
from flask.views import View, MethodView
from repast.util.session_common import set_session_dish,get_session_dish, get_session_value, get_session_user
from ...services.stores_service import get_stores_by_id
from ...services.dish_service import get_total_price
import time

class ToOrderDishes(View):
    '''to order dishes page'''
    methods = ('GET', 'POST')

    def render_template(self, content):
        '''render template'''
        return render_template('reception/extends_test.html', **content)

    def dispatch_request(self):
        '''return render_template'''
        content = {}
        return self.render_template(content)


def dish_selected():
    dish = get_session_dish()
    if dish is None:
        user_id = get_session_user()
        if user_id is None:
            user_id = request.args.get('user_id')
        dish = get_session_value(str(user_id))
    price = get_total_price(dish)
    package_id = request.args.get('package_id') # 当前套餐
    brand_id = request.args.get('brand_id') # 当前品牌
    stores_id = get_session_value('stores_id') # 当前餐厅
    stores = get_stores_by_id(stores_id)
    today = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    return render_template('reception/wdcaidan.html',
                           dish=dish,
                           stores=stores,
                           package_id=package_id,
                           brand_id=brand_id,
                           price=price,
                           today=today)

def to_pay_1():
    dish=get_session_dish()
    price=get_total_price(dish)
    return render_template('reception/pay1.html',
                           price = price)

def to_pay_5():
    dish=get_session_dish()
    price=get_total_price(dish)
    return render_template('reception/pay5.html',
                           price = price)