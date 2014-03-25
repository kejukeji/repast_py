# coding: UTF-8

from ..models.group import Group
from ..models.brand import Brand
from ..models.stores import Stores
from ..models.location import *
from flask.ext import restful
from ..util.session_common import *

class GetGroup(restful.Resource):
    '''获取集团'''
    @staticmethod
    def get():
        group = Group.query.filter().all()
        json = append_json(group)
        return json


class GetBrand(restful.Resource):
    '''获取品牌'''
    @staticmethod
    def get(group_id):
        brand = Brand.query.filter(Brand.group_id == group_id).all()
        json = append_json(brand)
        return json


class GetProvince(restful.Resource):
    '''获取省'''
    @staticmethod
    def get():
        province = Province.query.filter().all()
        json = append_json(province)
        return json

class GetCity(restful.Resource):
    '''获取市'''
    @staticmethod
    def get(province_id):
        city = City.query.filter(City.province_id == province_id).all()
        json = append_json(city)
        return json

class GetCounty(restful.Resource):
    '''获取区'''
    @staticmethod
    def get(city_id):
        county = County.query.filter(County.city_id == city_id).all()
        json = append_json(county)
        return json


class GetStores(restful.Resource):
    '''获取餐厅'''
    @staticmethod
    def get(brand_id):
        stores = Stores.query.filter(Stores.brand_id == brand_id).all()
        json = append_json(stores)
        return json


def append_json(model):
    json = []
    if model:
        for i in range(len(model)):
            json.append([model[i].id, model[i].name])
    return json