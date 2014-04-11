# coding: utf-8
from flask.ext.admin.contrib.sqla import ModelView
from flask import request
from repast.util.others import form_to_dict
from repast.services.dish_service import DishService

from repast.models.dish import Dish

class DishView(ModelView):
    '''dish '''
    page_size = 20
    can_create = True
    can_edit = True
    column_exclude_list = ('group_id', 'brand_id', 'dish_sort_id',)

    column_labels = dict(
        group_id = u'集团',
        group = u'集团',
        brand_id = u'品牌',
        brand = u'品牌',
        dish_sort_id = u'菜品类别',
        dish_sort = u'菜品类别',
        name = u'菜品名'
    )

    column_descriptions = dict(
        group_id = u'所属集团',
        group = u'所属集团',
        brand_id = u'所属品牌',
        brand = u'所属品牌',
        dish_sort_id = u'所属菜品类别',
        dish_sort = u'所属菜品类别',
        name = u'菜品名'
    )

    list_template = 'admin_page/dish_list.html'
    create_template = 'admin_page/dish_create.html'

    def scaffold_form(self):
        form_class = super(DishView, self).scaffold_form()
        delattr(form_class, 'group')
        delattr(form_class, 'brand')
        delattr(form_class, 'dish_sort')
        return form_class

    def create_model(self, form):
        form_dict = form_to_dict(form)
        success = DishService.create_dish(self.session, form_dict)
        return success

    def __init__(self, db, **kwargs):
        super(DishView, self).__init__(Dish, db, **kwargs)