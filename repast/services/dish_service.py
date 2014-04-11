# coding: utf-8
from base_service import BaseService

class DishService(BaseService):
    '''菜品'''
    def create_dish(self, session, form_dict, Object, args, special_args=None):
        return self.create_model(session, form_dict, Object, args, special_args)

    def update_dish(self, session, form_dict, model, args, special_args=None):
        self.update_model(session, form_dict, model, args, special_args)