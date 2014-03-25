# coding: UTF-8
from repast.models.group import Group
from repast.models.brand import Brand
from repast.models.stores import Stores

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