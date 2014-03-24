# coding: UTF-8
import logging
import os
from flask.ext.admin.contrib.sqla import ModelView
from flask import request


from wtforms.fields import TextAreaField, FileField
from repast.models.stores import Stores
from repast.services.stores_service import StoresService
from repast.util.others import form_to_dict

log = logging.getLogger("flask-admin.sqla")


class QueueSettingView(ModelView):
    '''桌型'''
    page_size = 20 # 条数
    can_create = True # 能否创建
    can_edit = True # 能否编辑


