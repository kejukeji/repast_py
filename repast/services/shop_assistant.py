# coding: UTF-8
from flask import flash
from flask.ext.admin.babel import gettext
import hashlib

from repast.models.queue import *
from repast.models.user import *
from repast.models.database import db
from .queue_setting_service import get_table_type_by_stores_id
from .common_service import GetName

class ShopAssistantService():
    '''店员'''
    @staticmethod
    def create_shop_assistant(session, form_dict):
        '''创建店员'''
        try:
            shop_assistant = ShopAssistantService._get_shop_assistant(form_dict) # 得到店员对象
            session.add(shop_assistant)
            session.commit()
        except Exception, ex:
            flash(gettext('Failed to create model. %(error)s', error=str(ex)), 'error')
            session.rollback()
            return False
        return True

    @staticmethod
    def update_shop_assistant(session, form_dict, model):
        '''修改店员'''
        try:
            group = GetName._get_group(form_dict)
            form_dict['group'] = group
            brand = GetName._get_brand(form_dict)
            form_dict['brand'] = brand
            stores = GetName._get_stores(form_dict)
            form_dict['stores'] = stores
            model.update(**form_dict)
            session.commit()
        except Exception, ex:
            flash(gettext('Failed to update model. %(error)s', error=str(ex)), 'error')
            session.rollback()
            return False
        return True

    @staticmethod
    def _get_shop_assistant(form_dict):
        '''根据后台表单中的值，创建 店员对象'''
        password = hashlib.new('md5', form_dict['password']).hexdigest()
        group = GetName._get_group(form_dict)
        brand = GetName._get_brand(form_dict)
        stores = GetName._get_stores(form_dict)
        shop_assistant = ShopAssistant(group_id=form_dict['group_id'],
                                       brand_id=form_dict['brand_id'],
                                       stores_id=form_dict['stores_id'],
                                       group=group,
                                       brand=brand,
                                       stores=stores,
                                       name=form_dict['name'],
                                       user_name=form_dict['user_name'],
                                       password=password,
                                       tel=form_dict['tel'])
        return shop_assistant



def get_shop_assistant_by_user(request):
    '''店员登录'''
    user_name = request.form.get('UserName')
    user_pass = request.form.get('Password')
    shop_assistant = ShopAssistant.query.filter(ShopAssistant.user_name == user_name, ShopAssistant.password == user_pass).first()
    return shop_assistant

def get_stores_id_by_shop_assistant_id(shop_assistant_id):
    '''根据员工id得到所属餐厅id'''
    shop_assistant = ShopAssistant.query.filter(ShopAssistant.id == shop_assistant_id).first()
    if shop_assistant:
        return shop_assistant.stores_id
    else:
        return 1


def call_number(queue_id):
    '''店员叫号'''
    queue = Queue.query.filter(Queue.id == queue_id).first()
    if queue:
        queue.status = 0 # 叫号修改状态值。说明已经叫过号
        try:
            db.commit()
        except:
            db.rollback()
            return False
    return True