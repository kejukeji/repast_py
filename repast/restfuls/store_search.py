#coding:UTF-8

from flask.ext import restful
from flask.ext.restful import reqparse
from repast.services.stores_service import *
from repast.util.others import flatten
from repast.util.get_distance import *
class SearchStore(restful.Resource):
    @staticmethod
    def get():
        para = reqparse.RequestParser()
        para.add_argument('keyword', type=str, required=False)


        args = para.parse_args()
        keyword = args.get('keyword')
        count = get_store_by_search_count(keyword)
        stores = get_store_by_search(keyword)
        dicts = {}
        dicts['stores'] = []
        if type(stores) is list:
            for s in stores:
                stores_pic = flatten(s)
                dicts['stores'].append(stores_pic)
        else:
            stores_pic = flatten(stores)
            dicts['stores'].append(stores_pic)
        print(dicts)
        return  dicts


class PositonStore(restful.Resource):
    @staticmethod
    def get():
        para = reqparse.RequestParser()
        para.add_argument('province', type=int, required=False)
        para.add_argument('city', type=int, required=False)
        para.add_argument('county', type=int, required=False)

        args = para.parse_args()
        province = args.get('province')
        city = args.get('city')
        county = args.get('county')
        count = get_store_by_position_count(province,city,county)
        stores = get_store_by_position(province,city,county)
        dicts = {}
        dicts['stores'] = []
        if type(stores) is list:
            for s in stores:
                stores_pic = flatten(s)
                dicts['stores'].append(stores_pic)
        else:
            if stores:
                stores_pic = flatten(stores)
                dicts['stores'].append(stores_pic)
        print(dicts)
        return  dicts

class PositonStoreXY(restful.Resource):
    @staticmethod
    def get():
        para = reqparse.RequestParser()
        para.add_argument('province', type=int, required=False)
        para.add_argument('city', type=int, required=False)
        para.add_argument('county', type=int, required=False)
        para.add_argument('latitude', type=float, required=False)
        para.add_argument('longitude', type=float, required=False)
        args = para.parse_args()
        province = args.get('province')
        city = args.get('city')
        county = args.get('county')
        latitude = args.get('latitude')
        longitude = args.get('longitude')
        count = get_store_by_position_count(province,city,county)
        stores = get_store_by_position(province,city,county)
        dicts = {}
        dicts['stores'] = []

        if type(stores) is list:
            sorteds = lambda stores: get_distance(latitude,longitude,stores.latitude,stores.longitude)
            store = sorted(stores,key=sorteds)

            for s in store:
                s.distance =  str(get_distance(latitude,longitude,s.latitude,s.longitude))[:6]
                stores_pic = flatten(s)
                dicts['stores'].append(stores_pic)
        else:
            if stores:
                lat = stores.latitude
                lng = stores.longitude
                d = str(get_distance(latitude,longitude,lat,lng))[:6]
                stores.distance = d
                stores_pic = flatten(stores)
                dicts['stores'].append(stores_pic)
        print(dicts)
        return  dicts