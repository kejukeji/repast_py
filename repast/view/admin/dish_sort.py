# coding: utf-8

from flask.ext.admin.contrib.sqla import ModelView
from repast.util.others import form_to_dict

class DishSort(ModelView):
    '''dish sort'''
    page_size = 20
    can_edit = True
    can_create = True

    column_labels = dict(

    )
