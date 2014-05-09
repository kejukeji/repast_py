#coding:utf-8
from repast.models.dish import *
from flask.ext import restful
from repast.util.others import flatten
from flask import request, render_template, redirect, url_for
from ..util.session_common import get_session_dish


class GetDishes(restful.Resource):
    """ 根据菜的种类获取菜单列表 """
    @staticmethod
    def get(dish_sort_id):
        package_id = request.args.get('package_id')
        if package_id:
            dishes = Dish.get_dish_by_kind_and_package(dish_sort_id, package_id)
        else:
            dishes = Dish.get_dish_by_kind_and_brand(dish_sort_id)
        json = append_json(dishes)
        return json


def append_json(model):
    json = {}
    json['dish'] = []
    json['dish_by_package'] = []
    json['total'] = 0
    dish = get_session_dish()
    if model:
        for i in range(len(model)):
            model_pic = flatten(model[i])
            json['dish'].append(model_pic)
    if dish:
        temp_total = 0
        for d in dish:
            temp_total = temp_total + d['price']
            json['dish_by_package'].append([d['id']])
        json['total'] = temp_total
    return json

