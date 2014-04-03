#coding:UTF-8

from repast.models.queue import *
from repast.models.database import *

def get_queue_count(store_id):
    return QueueSetting.query.filter(QueueSetting.stores_id==store_id).count()

def find_queue_by_store_id(store_id):
    count = QueueSetting.query.filter(QueueSetting.stores_id==store_id).count()
    if count == 1:
        restaurant = QueueSetting.query.filter(QueueSetting.stores_id==store_id).first()
    elif count > 1:
        restaurant = QueueSetting.query.filter(QueueSetting.stores_id==store_id).all()
    else:
        restaurant = ''
    return restaurant

def get_queue_by_id(queue_id):
    '''根据id得到桌型'''
    table_type = QueueSetting.query.filter(Queue.id == queue_id).first()
    return table_type

