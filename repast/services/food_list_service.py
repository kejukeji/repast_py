#coding:utf-8
from repast.models.dish import *
from flask.ext import restful


class GetDishes(restful.Resource):
    """ 根据菜的种类获取菜单列表 """
    @staticmethod
    def get_foods(dish_sort_id,brand_id):
        dishes = Dish.get_dish_by_kind_and_brand(dish_sort_id,brand_id)
        json = append_json(dishes)
        return json

def append_json(model):
     json = []
     if model:
        for i in range(len(model)):
            json.append([model[i].id, model[i].name])
     return json

