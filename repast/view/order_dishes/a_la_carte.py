#! /usr/bin/python
# coding: utf-8
from flask import render_template
from flask.views import View, MethodView

class ToOrderDishes(View):
    '''to order dishes page'''
    methods = ('GET', 'POST')

    def render_template(self, content):
        '''render template'''
        return render_template('home.html', **content)

    def dispatch_request(self):
        '''return render_template'''
        content = {}
        return self.render_template(content)

