# coding: UTF-8

from flask import flash
from flask.ext.admin.babel import gettext
import os
from werkzeug import secure_filename
from repast.models.queue import QueueSetting
from .common_service import *


class QueueService():
    '''桌型'''
    @staticmethod
    def create_queue_setting(session, form_dict):
        '''创建桌型'''
        try:
            queue_setting = QueueService.get_queue_setting(form_dict)
            session.add(queue_setting)
            session.commit()
        except Exception, ex:
            flash(gettext('Failed to create model. %(error)s', error=str(ex)), 'error')
            session.rollback()
            return False
        return True

    @staticmethod
    def update_queue_setting(session, form_dict, model):
        '''更新'''
        try:
            group_name = GetName._get_group(form_dict)
            form_dict['group'] = group_name
            brand_name = GetName._get_brand(form_dict)
            form_dict['brand'] = brand_name
            stores_name = GetName._get_stores(form_dict)
            form_dict['stores'] = stores_name
            model.update(**form_dict)
            session.commit()
        except Exception, ex:
            flash(gettext('Failed to update model. %(error)s', error=str(ex)), 'error')
            session.rollback()
            return False
        return True

    @staticmethod
    def get_queue_setting(form_dict):
        group = GetName._get_group(form_dict)
        brand = GetName._get_brand(form_dict)
        stores = GetName._get_stores(form_dict)
        return QueueSetting(group_id=form_dict['group_id'],
                            group=group,
                            brand_id=form_dict['brand_id'],
                            brand=brand,
                            stores_id=form_dict['stores_id'],
                            stores=stores,
                            type=form_dict['type'],
                            number=form_dict['number'])
