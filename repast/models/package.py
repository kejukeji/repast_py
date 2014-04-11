# coding: utf-8
from sqlalchemy import Column, String, Integer
from database import Base
from base_class import InitUpdate

PACKAGE = 'package'

class Package(Base, InitUpdate):
    __tablename__ = PACKAGE
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    group_id = Column(Integer, nullable=False)
    group = Column(String(50), nullable=False)
    brand_id = Column(Integer, nullable=False)
    brand = Column(String(50), nullable=False)
    dish_sort_id = Column(String(20), nullable=False)
    dish_sort = Column(String(200), nullable=False)
    suitable_number = Column(Integer, nullable=False, server_default='0')

    def __init__(self, **kwargs):
        args = ('name', 'group_id','group','brand_id','brand','dish_sort_id','dish_sort', 'suitable_number')
        self.init_value(args, kwargs)

    def update(self, **kwargs):
        args = ('name', 'group_id','group','brand_id','brand','dish_sort_id','dish_sort', 'suitable_number')
        self.update_value(args, kwargs)