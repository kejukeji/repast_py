# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import DOUBLE, FLOAT
from database import Base
from base_class import InitUpdate

DISH_SORT = 'dish_sort'
DISH = 'dish'

class DishSort(Base, InitUpdate):
    '''dish sort'''
    __tablename__ = DISH_SORT
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, nullable=False)
    group = Column(String(50), nullable=False)
    brand = Column(String(50), nullable=False)
    brand_id = Column(Integer, nullable=False)
    name = Column(String(50), nullable=True)

    def __init__(self, **kwargs):
        args = ('group', 'brand','name', 'group_id', 'brand_id')
        self.init_value(args, kwargs)

    def update(self, **kwargs):
        args = ('group', 'brand', 'name', 'group_id', 'brand_id')
        self.update_value(args, kwargs)


class Dish(Base, InitUpdate):
    '''dish'''
    __tablename__ = DISH
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    group_id = Column(Integer, nullable=False)
    group = Column(String(50), nullable=False)
    brand = Column(String(50), nullable=False)
    brand_id = Column(String(50), nullable=False)
    dish_sort_id = Column(Integer, nullable=False)
    dish_sort = Column(String(500), nullable=False)
    list_price = Column(FLOAT, nullable=False)
    price = Column(FLOAT, nullable=False)
    base_path = Column(String(500), nullable=True, server_default='')
    rel_path = Column(String(500), nullable=True, server_default='')
    picture_name = Column(String(500), nullable=True)

    def __init__(self, **kwargs):
        args = ('group_id', 'group', 'brand_id','brand', 'dish_sort_id', 'dish_sort', 'price', 'list_price', 'name', 'base_path', 'rel_path', 'picture_name')
        self.init_value(args, kwargs)

    def update(self, **kwargs):
        args = ('group_id', 'group', 'brand_id','brand', 'dish_sort_id', 'dish_sort', 'price', 'list_price', 'name','base_path', 'rel_path', 'picture_name')
        self.update_value(args, kwargs)