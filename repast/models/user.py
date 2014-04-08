# coding: UTF-8
from .database import Base
from .base_class import InitUpdate
from .group import Group
from .stores import Stores
from .brand import Brand
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.mysql import DOUBLE

USER = 'user'
SHOP_ASSISTANT = 'shop_assistant'

class User(Base, InitUpdate):
    '''用户'''
    __tablename__ = USER
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=True)
    nick_name = Column(String(20), nullable=True)
    password = Column(String(20), nullable=False, server_default='888888')
    openid = Column(String(200), nullable=False)
    picture_url = Column(String(500), nullable=True)
    longitude = Column(DOUBLE, nullable=True)
    latitude = Column(DOUBLE, nullable=True)
    description = Column(String(200), nullable=True)

    def __init__(self, **kwargs):
        args = ('nick_name','openid','picture_url')
        self.init_value(args, kwargs)

    def update(self, **kwargs):
        args = ('longitude','latitude', 'description')
        self.update_value(args,kwargs)


class ShopAssistant(Base, InitUpdate):
    '''店员'''
    __tablename__ = SHOP_ASSISTANT
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, nullable=False)
    group = Column(String(50), nullable=False)
    brand_id = Column(Integer, nullable=False)
    brand = Column(String(50), nullable=False)
    stores_id = Column(Integer, nullable=False)
    stores = Column(String(50), nullable=False)
    name = Column(String(20), nullable=False)
    user_name = Column(String(20), nullable=False)
    password = Column(String(200), nullable=False)
    tel = Column(String(12), nullable=True)

    def __init__(self, **kwargs):
        args = ('group_id','group','brand_id','brand','stores_id','stores','name','tel','user_name','password')
        self.init_value(args, kwargs)


    def update(self, **kwargs):
        args = ('group_id','group','brand_id','brand','stores_id','stores','name','tel','user_name','password')
        self.update_value(args, kwargs)
