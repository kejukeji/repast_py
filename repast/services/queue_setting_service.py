# coding: UTF-8

from flask import flash
from flask.ext.admin.babel import gettext
import os
from werkzeug import secure_filename
from repast.models.queue import QueueSetting, Queue
from .common_service import *
from repast.util.ex_time import *
from repast.models.database import db


class QueueService():
    '''桌型'''
    @staticmethod
    def create_queue_setting(session, form_dict):
        '''创建桌型'''
        try:
            queue_setting = QueueService.get_queue_setting(form_dict)
            session.add(queue_setting)
            session.commit()
        except Exception, ex:
            flash(gettext('Failed to create model. %(error)s', error=str(ex)), 'error')
            session.rollback()
            return False
        return True

    @staticmethod
    def update_queue_setting(session, form_dict, model):
        '''更新'''
        try:
            group_name = GetName._get_group(form_dict)
            form_dict['group'] = group_name
            brand_name = GetName._get_brand(form_dict)
            form_dict['brand'] = brand_name
            stores_name = GetName._get_stores(form_dict)
            form_dict['stores'] = stores_name
            model.update(**form_dict)
            session.commit()
        except Exception, ex:
            flash(gettext('Failed to update model. %(error)s', error=str(ex)), 'error')
            session.rollback()
            return False
        return True

    @staticmethod
    def get_queue_setting(form_dict):
        group = GetName._get_group(form_dict)
        brand = GetName._get_brand(form_dict)
        stores = GetName._get_stores(form_dict)
        return QueueSetting(group_id=form_dict['group_id'],
                            group=group,
                            brand_id=form_dict['brand_id'],
                            brand=brand,
                            stores_id=form_dict['stores_id'],
                            stores=stores,
                            type=form_dict['type'],
                            number=form_dict['number'])


def check_queue_by_user_id_and_stores_id(user_id, stores_id, table_type_id):
    '''根据user_id,stores_id判断是否已经存在'''
    args_time = get_date_time_str()
    queue = Queue.query.filter(Queue.user_id == user_id, Queue.stores_id == stores_id, Queue.queue_setting_id == table_type_id, Queue.queue_time.like(args_time)).first()
    if queue:
        return queue
    return None

def get_date_time_str():
    now_time = todayfstr() # 当前时间
    str_time = str(now_time)[:10] # 截取当前时间。去掉时分秒
    args_time = '%'+ str_time +'%'
    return args_time


def create_queue(user_id, stores_id, table_type_id):
    '''根据当前时间得到队列'''
    args_time = get_date_time_str()
    queue_count = Queue.query.filter(Queue.queue_time.like(args_time)).count()
    queue = None
    if queue_count == 1:
        queue = Queue.query.filter(Queue.queue_time.like(args_time)).first() # 得到队列中最后一个
        next_number = queue.now_queue_number + 1 # 得到下一个队列号
        new_queue = get_queue(user_id,stores_id,table_type_id,next_number)
        create_new_queue(new_queue)
    elif queue_count > 1:
        queue = Queue.query.filter(Queue.queue_time.like(args_time)).order_by(Queue.queue_time.desc()).first()# 得到已经存在的队列
        next_number = queue.now_queue_number + 1 # 得到下一个队列号
        new_queue = get_queue(user_id,stores_id,table_type_id,next_number)
        create_new_queue(new_queue)
    if queue_count == 0:
        queue = get_queue(user_id,stores_id,table_type_id, 1) # 如果当前没有队列，那么就创建一个新队列并为第一个
        create_new_queue(queue)
    return queue


def get_queue(user_id, stores_id, table_type_id, next_number):
    '''创建队列'''
    queue = Queue(queue_setting_id=table_type_id,
                  now_queue_number=next_number,
                  user_id=user_id,
                  stores_id=stores_id)
    return queue

def cancel(queue_id):
    '''取消队列'''
    queue = Queue.query.filter(Queue.id == queue_id).first()
    queue.status = 0
    db.commit()


def create_new_queue(model):
    '''创建新model'''
    db.add(model)
    db.commit()