# coding: UTF-8
from repast.models.group import Group
from repast.models.brand import Brand
from repast.models.stores import Stores
from repast.models.dish import DishSort

class GetName():
    @staticmethod
    def _get_group(form_dict):
            '''获取所属集团'''
            group = Group.query.filter(Group.id == form_dict['group_id']).first()
            group_name = ''
            if group:
                group_name = group.name
            return group_name
    @staticmethod
    def _get_brand(form_dict):
            '''获取所属集团'''
            brand = Brand.query.filter(Brand.id == form_dict['brand_id']).first()
            brand_name = ''
            if brand:
                brand_name = brand.name
            return brand_name
    @staticmethod
    def _get_stores(form_dict):
        '''获取所属餐厅'''
        stores = Stores.query.filter(Stores.id == form_dict['stores_id']).first()
        stores_name = ''
        if stores:
            stores_name = stores.name
        return stores_name

    @staticmethod
    def _get_dish_sort(form_dict):
        dish_sort_name = ''
        dish_sort_id_array = form_dict['dish_sort_id']
        if type(dish_sort_id_array) is list:
            for item in form_dict['dish_sort_id']:
                dish_sort = DishSort.query.filter(DishSort.id == item).first()
                dish_sort_name = dish_sort_name + ',' + dish_sort.name
        else:
            dish_sort = DishSort.query.filter(DishSort.id == dish_sort_id_array).first()
            dish_sort_name = dish_sort.name
        return dish_sort_name

    @staticmethod
    def _get_dish_sort_id(form_dict):
        dish_sort_id = ''
        dish_sort_id_array = form_dict['dish_sort_id']
        if type(dish_sort_id_array) is list:
            for item in form_dict['dish_sort_id']:
                dish_sort_id = dish_sort_id + ',' + item
        else:
            dish_sort_id = dish_sort_id_array
        return dish_sort_id