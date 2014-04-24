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

    @staticmethod
    def get_dish_sort_by_id(dish_sort_id):
        dish_sort = DishSort.query.filter(DishSort.id == dish_sort_id).first()
        return dish_sort

    @staticmethod
    def get_dish_sort_by_brand(brand_id):
        dish_sort = DishSort.query.filter(DishSort.brand_id == brand_id).all()
        return dish_sort


class Dish(Base, InitUpdate):
    '''dish'''
    __tablename__ = DISH
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    group_id = Column(Integer, nullable=False)
    group = Column(String(50), nullable=False)
    brand = Column(String(50), nullable=False)
    brand_id = Column(String(50), nullable=False)
    package = Column(String(50), nullable=False)
    package_id = Column(Integer, nullable=False)
    dish_sort_id = Column(Integer, nullable=False)
    dish_sort = Column(String(500), nullable=False)
    list_price = Column(FLOAT, nullable=False)
    price = Column(FLOAT, nullable=False)
    base_path = Column(String(500), nullable=True, server_default='')
    rel_path = Column(String(500), nullable=True, server_default='')
    picture_name = Column(String(500), nullable=True)

    def __init__(self, **kwargs):
        args = ('group_id', 'group', 'brand_id','brand', 'dish_sort_id', 'dish_sort', 'price', 'list_price', 'name', 'base_path', 'rel_path', 'picture_name', 'package_id', 'package')
        self.init_value(args, kwargs)

    def update(self, **kwargs):
        args = ('group_id', 'group', 'brand_id','brand', 'dish_sort_id', 'dish_sort', 'price', 'list_price', 'name','base_path', 'rel_path', 'picture_name', 'package_id', 'package')
        self.update_value(args, kwargs)

    @staticmethod
    def get_dish_by_package(package):
        temp = []
        dish_count = Dish.query.filter(Dish.brand_id == package.brand_id, Dish.package_id == package.id).count()
        if dish_count > 1:
            dish = Dish.query.filter(Dish.brand_id == package.brand_id, Dish.package_id == package.id).all()
            for d in dish:
                temp.append(d)
        else:
            dish = Dish.query.filter(Dish.brand_id == package.brand_id, Dish.package_id == package.id).first()
            if dish:
                temp.append(dish)
        return temp

    @staticmethod
    def get_dish_by_kind_and_brand(dish_sort_id, brand_id):
        '''根据分类和品牌获取所有分类的菜品'''
        temp = []
        dish_count = Dish.query.filter(Dish.dish_sort_id == dish_sort_id, Dish.brand_id == brand_id).count()
        if dish_count > 1:
            dish = Dish.query.filter(Dish.dish_sort_id == dish_sort_id, Dish.brand_id == brand_id).all()
            for d in dish:
                temp.append(d)
        else:
            dish = Dish.query.filter(Dish.dish_sort_id == dish_sort_id, Dish.brand_id == brand_id).first()
            if dish:
                temp.append(dish)
        return temp