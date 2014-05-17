#! /usr/bin/python
# coding: utf-8
from flask import render_template, request
from flask.views import View, MethodView
from repast.util.session_common import set_session_dish,get_session_dish, get_session_value
from ...services.stores_service import get_stores_by_id

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
    package_id = request.args.get('package_id') # 当前套餐
    brand_id = request.args.get('brand_id') # 当前品牌
    stores_id = get_session_value('stores_id') # 当前餐厅
    stores = get_stores_by_id(stores_id)
    return render_template('reception/wdcaidan.html',
                           dish=dish,
                           stores=stores,
                           package_id=package_id,
                           brand_id=brand_id)
