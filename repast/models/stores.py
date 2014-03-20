# coding: UTF-8

from .database import Base
from .base_class import InitUpdate
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.dialects.mysql import DOUBLE
from .group import Group
from .brand import Brand
from .location import Province, City, County

STORES = 'stores'
STORES_INFO = 'stores_info'

class Stores(Base, InitUpdate):
    '''餐厅'''
    __tablename__ = STORES
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=True)
    address = Column(String(100), nullable=False)
    longitude = Column(DOUBLE, nullable=False)
    latitude = Column(DOUBLE, nullable=False)
    brand_id = Column(Integer,ForeignKey(Brand.id, ondelete='cascade', onupdate='cascade'))
    brand = Column(String(50), nullable=False)
    recommend = Column(Boolean, nullable=False, server_default='0') # 0不推荐，1推荐
    manager = Column(String(20), nullable=False)
    tel = Column(String(20), nullable=False)
    group_id = Column(Integer, ForeignKey(Group.id, ondelete='cascade', onupdate='cascade'))
    group = Column(String(50), nullable=False)
    province_id = Column(Integer, ForeignKey(Province.id, ondelete='cascade', onupdate='cascade'))
    city_id = Column(Integer, ForeignKey(City.id, ondelete='cascade', onupdate='cascade'))
    county_id = Column(Integer, ForeignKey(County.id, ondelete='cascade', onupdate='cascade'))

    def __index__(self, **kwargs):
        '''初始化'''
        args = ('name','address','longitude','latitude','brand_id','brand','recommend','manager',
        'tel','group_id','group','province_id','city_id','county_id')
        self.init_value(args, kwargs)

class StoresInfo(Base,InitUpdate):
    '''详细信息'''
    __tablename__ = STORES_INFO
    id = Column(Integer, primary_key=True)
    stores_id = Column(Integer, ForeignKey(Stores.id, ondelete='cascade', onupdate='cascade'))
    base_path = Column(String(200), nullable=False)
    rel_path = Column(String(200), nullable=False)
    picture_name = Column(String(300), nullable=False)

    def __init__(self, **kwargs):
        '''初始化'''
        args = ('stores_id','base_path','rel_path','picture_name')
        self.init_value(args, kwargs)