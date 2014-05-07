#! /usr/bin/python
# coding: utf-8
from flask import render_template
from flask.views import View, MethodView
from repast.util.session_common import set_session_dish,get_session_dish
from repast.services.order_dish_service import PackageServiceView

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
    return render_template('reception/wdcaidan.html',
                           dish=dish)
