#coding:utf-8
from repast.models.dish import *
from flask.ext import restful
from repast.util.others import flatten
from flask import request, render_template, redirect, url_for


class GetDishes(restful.Resource):
    """ 根据菜的种类获取菜单列表 """
    @staticmethod
    def get(dish_sort_id):
        package_id = request.args.get('package_id')
        #if package_id:
        #    dishes = Dish.get_dish_by_kind_and_package(dish_sort_id)
        #else:
        dishes = Dish.get_dish_by_kind_and_brand(dish_sort_id)
        json = append_json(dishes)
        return json


def append_json(model):
     json = {}
     json['dish'] = []
     if model:
        for i in range(len(model)):
            model_pic = flatten(model[i])
            json['dish'].append(model_pic)
     return json

