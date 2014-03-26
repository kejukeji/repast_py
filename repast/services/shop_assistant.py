# coding: UTF-8

from repast.models.queue import *
from repast.models.user import *


def get_shop_assistant_by_user(request):
    '''店员登录'''
    user_name = request.form.get('name')
    user_pass = request.form.get('password')
    shop_assistant = ShopAssistant.query.filter(ShopAssistant.name == user_name, ShopAssistant.password == user_pass).first()
    return shop_assistant

