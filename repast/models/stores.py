# coding: UTF-8

from .database import Base
from .base_class import InitUpdate
from sqlalchemy import Column, Integer, String

STORES = 'stores'

class Stores(Base, InitUpdate):
    '''餐厅'''
    __tablename__ = STORES
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=True)
