# coding: UTF-8
from .database import Base
from .base_class import InitUpdate
from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME,Boolean
from .stores import Stores
from .user import User

QUEUE_SETTING = 'queue_setting'
QUEUE = 'queue'

class QueueSetting(Base, InitUpdate):
    '''队列，每个餐厅的座位种类，每个种类有多少个座位'''
    __tablename__ = QUEUE_SETTING
    id = Column(Integer, primary_key=True)
    type = Column(String(5), nullable=False)
    number = Column(Integer, nullable=False)
    stores_id = Column(Integer, ForeignKey(Stores.id, ondelete='cascade', onupdate='cascade'))
    status = Column(Integer, nullable=False, server_default='0')

    def __init__(self, **kwargs):
        args = ('type','number','stores_id','status')
        self.init_value(args, kwargs)


class Queue(Base,InitUpdate):
    '''排队'''
    __tablename__ = QUEUE
    id = Column(Integer, primary_key=True)
    queue_setting_id = Column(Integer, ForeignKey(QueueSetting.id, ondelete='cascade', onupdate='cascade'))
    queue_time = Column(DATETIME, nullable=False)
    now_queue_number = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False, server_default='0')
    user_id = Column(Integer, ForeignKey(User.id, ondelete='cascade', onupdate='cascade'))

    def __init__(self, **kwargs):
        args = ('queue_setting_id','queue_time','now_queue_number')
        self.init_value(args, kwargs)
