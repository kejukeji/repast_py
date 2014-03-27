# coding: UTF-8

from repast.models.queue import *
from repast.models.user import *
from repast.models.database import db


def get_shop_assistant_by_user(request):
    '''店员登录'''
    user_name = request.form.get('name')
    user_pass = request.form.get('password')
    shop_assistant = ShopAssistant.query.filter(ShopAssistant.name == user_name, ShopAssistant.password == user_pass).first()
    return shop_assistant


def call_number(queue_id):
    '''店员叫号'''
    queue = Queue.query.filter(Queue.id == queue_id).first()
    if queue:
        queue.status = 0 # 叫号修改状态值。说明已经叫过号
        try:
            db.commit()
        except:
            db.rollback()
    return True